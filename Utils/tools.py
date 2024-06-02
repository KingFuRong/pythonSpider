import base64
import random
import time

import cv2
from PIL import Image


def time_now():
    return int(time.time() * 1000)


def download_img(session, name, url):
    response = session.get(url)
    with open(f'{name}.jpg', 'wb') as f:
        f.write(response.content)


def revert_img(path):
    old_img = Image.open(path)
    new_img = Image.new('RGB', (260, 160))

    Ut = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43, 42, 12,
          13, 23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]
    r = 160
    a = 80
    for _ in range(52):
        c = Ut[_] % 26 * 12 + 1
        u = a if 25 < Ut[_] else 0
        l = old_img.crop((c, u, c + 10, u + a))
        new_img.paste(l, (_ % 26 * 10, a if 25 < _ else 0))
    new_img.save(f'new_{path}')


def find_location(slide_img, bg_img, check=False):
    # 读取背景图和滑块图
    bg = cv2.imread(bg_img)
    slice = cv2.imread(slide_img)

    # 对图片做灰度处理
    bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
    slice = cv2.cvtColor(slice, cv2.COLOR_BGR2GRAY)

    # 对图片进行边缘处理
    bg = cv2.Canny(bg, 100, 200)
    slice = cv2.Canny(slice, 100, 200)

    # 匹配图片相似度
    result = cv2.matchTemplate(bg, slice, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if check:
        cv2.rectangle(bg, (max_loc[0], max_loc[1]), (max_loc[0] + 50, max_loc[1] + 50), (255, 255, 255))
        cv2.imshow('bg', bg)
        cv2.imshow('slice', slice)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return max_loc[0]


def base64_to_image(base64_str, image_path):
    img_data = base64.b64decode(base64_str)
    with open(image_path, 'wb') as f:
        f.write(img_data)


def __ease_out_expo(sep):
    """
    缓动函数 easeOutExpo
    参考：https://easings.net/zh-cn#easeOutExpo
    """
    if sep == 1:
        return 1
    else:
        return 1 - pow(2, -10 * sep)


def get_slide_track(distance):
    """
    根据滑动距离生成滑动轨迹
    :param distance: 需要滑动的距离
    :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
        x: 已滑动的横向距离
        y: 已滑动的纵向距离, 除起点外, 均为0
        t: 滑动过程消耗的时间, 单位: 毫秒
    """

    if not isinstance(distance, int) or distance < 0:
        raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
    # 初始化轨迹列表
    slide_track = [
        [random.randint(-50, -10), random.randint(-50, -10), 0],
        [0, 0, 0],
    ]
    # 共记录count次滑块位置信息
    count = 30 + int(distance / 2)
    # 初始化滑动时间
    t = random.randint(50, 100)
    # 记录上一次滑动的距离
    _x = 0
    _y = 0
    for i in range(count):
        # 已滑动的横向距离
        x = round(__ease_out_expo(i / count) * distance)
        # 滑动过程消耗的时间
        t += random.randint(10, 20)
        # if x == _x:
        #     continue
        slide_track.append([x, _y, t])
        _x = x
    slide_track.append(slide_track[-1])
    return slide_track, t
