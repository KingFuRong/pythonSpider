# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random

import execjs
from scrapy.http import HtmlResponse
# useful for handling different item types with a single interface
from aqistudy.settings import USER_AGENT_LIST


def get_month_data(item):
    return {'city': item.get('city_name')}


def get_day_data(item):
    return {
        'city': item.get('city_name'),
        'month': item.get('city_month'),
    }


# 随机请求头
class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        random_user_agent = random.choice(USER_AGENT_LIST)
        request.headers['User-Agent'] = random_user_agent
        return None


class GenerationhA4Nse2cTMiddleware(object):
    # api访问必备参数生成
    def process_request(self, request, spider):
        # print(request.url, request.method)
        if 'processed' in request.meta:
            return None
        elif request.method == 'POST':
            status_to_func = {
                'GETMONTHDATA': get_month_data,
                'GETDAYDATA': get_day_data,
            }
            item = request.meta['item']
            status = item.get('request_status')
            func = status_to_func.get(status)

            if func is not None:
                m0fhOhhGL = status
                oBDNNVgaDf = func(item)

                with open('./aqistudy/javascripts/generation_hA4Nse2cT.js', 'r') as f:
                    js_file = f.read()
                hA4Nse2cT = execjs.compile(js_file).call('generation_hA4Nse2cT', m0fhOhhGL, oBDNNVgaDf)
                data = {'hA4Nse2cT': hA4Nse2cT}  # 这是你要添加的数据
                item = request.meta['item']
                request = request.replace(formdata=data, meta={'processed': True, 'item': item})
                return request
            else:
                return None

    # 响应解密
    def process_response(self, request, response, spider):
        if 'processed' in request.meta:
            with open('./aqistudy/javascripts/generation_hA4Nse2cT.js', 'r') as f:
                js_file = f.read()
            data = execjs.compile(js_file).call('decode_data', response.body.decode('utf-8'))
            print(response.body.decode('utf-8'))
            print(data)
            new_response = HtmlResponse(url=request.url, body=data, encoding='utf-8', request=request)
            return new_response
        else:
            return response
