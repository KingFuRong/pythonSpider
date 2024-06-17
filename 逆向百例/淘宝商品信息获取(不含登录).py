import json

import requests
import hashlib
import time

from itertools import product

headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://item.taobao.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://item.taobao.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}
cookies = {
    "cookie2": "填自己的",
    "wk_cookie2": "填自己的",
    "wk_unb": "填自己的",
    "unb": "填自己的",
    "sg": "填自己的",
}
base_url = "https://h5api.m.taobao.com/h5/mtop.taobao.pcdetail.data.get/1.0/"


def update_cookies():
    time_stamp = str(int(time.time() * 1000))
    data_info = ("{\"params\":\"{\\\"resId\\\":\\\"33799945\\\",\\\"bizId\\\":\\\"443\\\","
                 "\\\"fromUrl\\\":\\\"https://www.taobao.com/\\\"}\"}")
    token = 'undefined'
    url = "https://h5api.m.taobao.com/h5/mtop.tmall.kangaroo.core.service.route.aldlampservicefixedresv2/1.0/"
    params = {
        "appKey": "12574478",
        "t": time_stamp,
        "sign": hashlib.md5((token + "&" + time_stamp + "&" + '12574478' + "&" + data_info).encode()).hexdigest(),
        "data": data_info
    }
    response = requests.get(url, headers=headers, params=params)
    cookie = response.cookies.get_dict()  # _m_h5_tk  _m_h5_tk_enc
    cookies.update(cookie)


def update_sgcookie():
    time_stamp = str(int(time.time() * 1000))
    data_info = ("{\"params\":\"{\\\"resId\\\":\\\"10760644\\\",\\\"bizId\\\":\\\"20200922\\\","
                 "\\\"source\\\":\\\"tianhe_taobao_pc_1\\\",\\\"count\\\":3,\\\"platform\\\":\\\"pc\\\"}\"}")
    token = cookies['_m_h5_tk'].split('_')[0]
    url = "https://h5api.m.taobao.com/h5/mtop.tmall.kangaroo.core.service.route.aldlampservicefixedresv2/1.0/"
    params = {
        "appKey": "12574478",
        "t": time_stamp,
        "sign": hashlib.md5((token + "&" + time_stamp + "&" + '12574478' + "&" + data_info).encode()).hexdigest(),
        "data": data_info
    }
    response = requests.get(url, headers=headers, params=params, cookies=cookies)
    cookie = response.cookies.get_dict()
    cookies['sgcookie'] = cookie['sgcookie']


def get_data(item_id):
    time_stamp = str(int(time.time() * 1000))
    data_info = ("{\"id\":\"item_id\",\"detail_v\":\"3.3.2\",\"exParams\":\"{"
                 "\\\"spm\\\":\\\"a21bo.jianhua/a.201876.d37.5af92a89I61ERe\\\",\\\"id\\\":\\\"item_id\\\","
                 "\\\"scm\\\":\\\"1007.40986.369799.0\\\",\\\"pvid\\\":\\\"232c8d2b-d645-45d6-b9ad-60e321fbf8bc\\\","
                 "\\\"queryParams\\\":\\\"id=item_id&pvid=232c8d2b-d645-45d6-b9ad-60e321fbf8bc&scm=1007.40986"
                 ".369799.0&spm=a21bo.jianhua%2Fa.201876.d37.5af92a89I61ERe\\\","
                 "\\\"domain\\\":\\\"https://item.taobao.com\\\",\\\"path_name\\\":\\\"/item.htm\\\"}\"}").replace(
        'item_id', str(item_id))
    token = cookies['_m_h5_tk'].split('_')[0]
    params = {
        "appKey": "12574478",
        "t": time_stamp,
        "sign": hashlib.md5((token + "&" + time_stamp + "&" + '12574478' + "&" + data_info).encode()).hexdigest(),
        "ttid": "2022@taobao_litepc_9.17.0",
        "data": data_info
    }
    response = requests.get(base_url, headers=headers, cookies=cookies, params=params)
    return response.json()


def none_group(item_kind_info_group):
    discount_group = []
    item_kind_info = item_kind_info_group.get('0')
    status = item_kind_info.get('quantityText')  # 商品状态 -> 有货 or 无货
    price = item_kind_info.get('price').get('priceText')
    if item_kind_info.get('itemApplyParams') is not None:
        discount_group.append(json.loads(item_kind_info.get('itemApplyParams'))[0]['couponName'])
        after_discount = item_kind_info.get('subPrice')
        after_discount_price = after_discount.get('priceText')
        after_discount_title = after_discount.get('priceTitle')
        print(f'\t商品价格:{price}元')
        print(f'\t商品状态:{status}')
        print(f'\t{after_discount_title}:{after_discount_price}元')
    else:
        print(f'\t商品价格:{price}元')
        print(f'\t商品状态:{status}')
    discount_group = list(set(discount_group))
    return discount_group


def one_group(item_kind_info_group, item_kind_id_group):
    item_kind_info_group = item_kind_info_group.get("sku2info")  # 分类详细信息
    item_kinds_name = item_kind_id_group.get('props')[0].get('name')  # 分类名称
    item_kinds_id = item_kind_id_group.get('props')[0].get('pid')  # 分类id
    item_skus_group = item_kind_id_group.get('skus')  # 每一个子类的skuId

    original_info_list = []
    discount_group = []

    for info in item_kind_id_group.get('props')[0].get('values'):
        info_dict = {'name': info.get('name'),
                     'image': info.get('image'),
                     'propPath': f'{item_kinds_id}:{info.get("vid")}'}
        for i in range(len(item_skus_group)):
            if item_skus_group[i]['propPath'] == info_dict['propPath']:
                info_dict['skuId'] = item_skus_group[i]['skuId']
                item_skus_group.pop(i)
                break
        original_info_list.append(info_dict)

    for i in range(len(original_info_list)):
        item_kind_info = item_kind_info_group.get(original_info_list[i]['skuId'])
        status = item_kind_info.get('quantityText')  # 商品状态 -> 有货 or 无货
        price = item_kind_info.get('price').get('priceText')
        if item_kind_info.get('itemApplyParams') is not None:
            discount_group.append(json.loads(item_kind_info.get('itemApplyParams'))[0]['couponName'])
            after_discount = item_kind_info.get('subPrice')
            after_discount_price = after_discount.get('priceText')
            after_discount_title = after_discount.get('priceTitle')
            original_info_list[i].update(
                {'status': status, 'price': price, 'after_discount_title': after_discount_title,
                 'after_discount_price': after_discount_price})
        else:
            original_info_list[i].update({'status': status, 'price': price})

    print(f'\t商品子类名称:{item_kinds_name}')
    for kind in original_info_list:
        if str(kind).find('券后') or str(kind).find('折后'):
            print(
                f'\t\t名称:{kind["name"]},价格:{kind["price"]}元,状态:{kind["status"]},{kind["after_discount_title"]}:{kind["after_discount_title"]}元')
        else:
            print(f'\t\t名称:{kind["name"]},价格:{kind["price"]}元,状态:{kind["status"]}')

    discount_group = list(set(discount_group))
    return discount_group


def multi_group(item_kind_info_group, item_kind_id_group):
    item_kind_info_group = item_kind_info_group.get("sku2info")  # 分类详细信息
    props_group = item_kind_id_group.get('props')
    item_skus_group = item_kind_id_group.get('skus')
    original_info_list = []
    for prop in props_group:
        prop_name = prop.get('name')
        prop_pid = prop.get('pid')
        prop_values = prop.get('values')
        prop_info_group = []
        for value in prop_values:
            value_name = value.get('name')
            value_vid = value.get('vid')
            value_propPath = prop_pid + ':' + value_vid
            prop_info_group.append({'name': value_name, 'propPath': value_propPath})
        original_info_list.append({'name': prop_name, 'prop_info': prop_info_group})

    print('\t\t', end='')
    for name in original_info_list:
        print(name['name'], end='\t')
    print(f'价格\t状态')

    prop_info_lists = [item['prop_info'] for item in original_info_list]
    combinations = list(product(*prop_info_lists))
    discount_group = []

    for final_info in combinations:
        name = ''
        propPath = ''
        for info in final_info:
            name += info['name'] + '\t'
            propPath += info['propPath'] + ';'
        propPath = propPath[:-1]
        for i in range(len(item_skus_group)):
            if item_skus_group[i]['propPath'] == propPath:
                skuId = item_skus_group[i]['skuId']
                item_skus_group.pop(i)
                break
        item_kind_info = item_kind_info_group.get(skuId)
        status = item_kind_info.get('quantityText')  # 商品状态 -> 有货 or 无货
        price = item_kind_info.get('price').get('priceText')

        if item_kind_info.get('itemApplyParams') is not None:
            discount_group.append(json.loads(item_kind_info.get('itemApplyParams'))[0]['couponName'])
            after_discount = item_kind_info.get('subPrice')
            after_discount_price = after_discount.get('priceText')
            after_discount_title = after_discount.get('priceTitle')
            print('\t\t', name, price + '元', status, after_discount_title, after_discount_price + '元')
        else:
            print('\t\t', name, price + '元', status)

    discount_group = list(set(discount_group))
    return discount_group


def processiong_data(item_data):
    true_data = item_data.get("data")

    item_base_info = true_data.get("item")
    item_title = item_base_info.get("title")  # 商品标题
    item_description_image = item_base_info.get("images")  # 商品主图
    item_sell_count = item_base_info.get("vagueSellCount")  # 商品销量

    print('商品基本信息:')
    print(f'\t商品标题:{item_title}')
    print(f'\t商品主图链接:{item_description_image}')
    print(f'\t商品销量:{item_sell_count}')

    item_kind_info_group = true_data.get("skuCore")
    item_kind_id_group = true_data.get("skuBase")

    if item_kind_id_group.get('props') is None:
        discount = none_group(item_kind_info_group)
    elif len(item_kind_id_group.get('props')) == 1:
        discount = one_group(item_kind_info_group, item_kind_id_group)
    else:
        discount = multi_group(item_kind_info_group, item_kind_id_group)

    discount_info = true_data.get('componentsVO').get('priceVO').get('extraPrice')
    print('优惠券信息:')
    if discount is not None:
        for item in discount:
            print('\t' + item)
    if discount_info is not None:
        print(
            f'\t{discount_info.get("priceTitle")} {discount_info.get("priceText")}元 {discount_info.get("priceDesc")}')


if __name__ == '__main__':
    item_id = input('请输入商品id:')
    update_cookies()
    update_sgcookie()
    item_data = get_data(item_id)
    processiong_data(item_data)
