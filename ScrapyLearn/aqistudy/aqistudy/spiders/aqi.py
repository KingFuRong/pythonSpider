import json
import time

import scrapy
from aqistudy.items import AqistudyItem


class AqiSpider(scrapy.Spider):
    name = "aqi"
    allowed_domains = ["aqistudy.cn"]
    start_urls = ["https://www.aqistudy.cn/historydata/"]

    def parse(self, response):
        city_list = response.xpath('//ul[@class="unstyled"]/div/li/a')
        for city in city_list:
            item = AqistudyItem()
            item['city_name'] = city.xpath('.//text()').get()
            item['city_url'] = response.urljoin(city.xpath('.//@href').get())
            item['request_status'] = "GETMONTHDATA"
            yield scrapy.FormRequest(
                url='https://www.aqistudy.cn/historydata/api/historyapi.php',
                formdata={'city': item['city_name']},
                method='POST',
                meta={'item': item},
                callback=self.city_parse,
            )

    def city_parse(self, response):
        item = response.meta['item']
        json_data = json.loads(response.body.decode('utf-8'))

        formatted_json = json.dumps(json_data, indent=4, ensure_ascii=False)
        print(item["city_name"])
        with open(f'./res/{item["city_name"]}.json', 'w', encoding='utf-8') as f:
            f.write(formatted_json)
        # pass

