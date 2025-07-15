import base64
import json
import re
import time

import cv2
import numpy as np

import requests

import random


class HumanizedBestFitSlider:
    """
    一个基于最佳匹配模板、高度仿生的滑块轨迹生成器 (V7 - 最终正确版)。

    此版本解决了所有先前模型的根本性逻辑缺陷，通过智能选择最合适的模板来确保
    在任何距离下的高度保真度。

    核心策略:
    1.  **模板库预分析**: 内置并预处理所有真实轨迹，计算每个模板的特征，
        特别是其总位移向量和标量距离。
    2.  **最佳匹配选择**: 在生成前，根据目标距离，从库中找出总距离最接近的模板。
        这确保了长距离任务使用长模板，短距离任务使用短模板。
    3.  **特征保留缩放**: 仅对选中的最佳匹配模板进行缩放和随机化，最大程度保留
        其固有的、真实的运动节奏。
    4.  **像素级精确修正**: 最终对轨迹进行微调，确保终点绝对准确。
    """

    def __init__(self, target_xy, randomness_factor=0.3):
        """
        初始化生成器。
        :param target_xy: (x, y) 轨迹的目标终点（相对于起点(0,0)）。
        :param randomness_factor: 随机扰动系数。
        """
        self.target_xy = np.array(target_xy, dtype=float)
        self.target_distance = np.linalg.norm(self.target_xy)
        self.randomness = randomness_factor
        self.templates_data = self._load_and_analyze_templates()
        self.best_template, self.chosen_template_index = self._find_best_template()

    def _preprocess_raw_template(self, raw_track):
        """将原始的绝对坐标轨迹转换为 [dx, dy, dt] 的差值格式。"""
        # 忽略第一个浏览器固定写入的点
        track_points = np.array(raw_track[1:], dtype=np.int64)
        offsets = track_points[1:, :2] - track_points[:-1, :2]
        dts = track_points[1:, 2] - track_points[:-1, 2]
        delta_track = np.c_[offsets, dts]
        return delta_track[delta_track[:, 2] > 0]

    def _load_and_analyze_templates(self):
        """加载所有原始轨迹，进行预处理，并计算每个模板的特征。"""
        raw_templates = [
            # Trajectory 1
            [
                [
                    "754",
                    "280",
                    1752550659206
                ],
                [
                    "783",
                    "302",
                    1752550659206
                ],
                [
                    "783",
                    "302",
                    1752550659399
                ],
                [
                    "784",
                    "302",
                    1752550659415
                ],
                [
                    "785",
                    "302",
                    1752550659432
                ],
                [
                    "787",
                    "302",
                    1752550659452
                ],
                [
                    "789",
                    "302",
                    1752550659465
                ],
                [
                    "792",
                    "302",
                    1752550659482
                ],
                [
                    "796",
                    "302",
                    1752550659500
                ],
                [
                    "800",
                    "302",
                    1752550659517
                ],
                [
                    "803",
                    "301",
                    1752550659536
                ],
                [
                    "806",
                    "301",
                    1752550659551
                ],
                [
                    "809",
                    "300",
                    1752550659566
                ],
                [
                    "811",
                    "299",
                    1752550659584
                ],
                [
                    "815",
                    "298",
                    1752550659601
                ],
                [
                    "818",
                    "297",
                    1752550659616
                ],
                [
                    "822",
                    "296",
                    1752550659633
                ],
                [
                    "825",
                    "296",
                    1752550659649
                ],
                [
                    "828",
                    "295",
                    1752550659665
                ],
                [
                    "830",
                    "294",
                    1752550659682
                ],
                [
                    "833",
                    "293",
                    1752550659701
                ],
                [
                    "835",
                    "293",
                    1752550659718
                ],
                [
                    "837",
                    "292",
                    1752550659734
                ],
                [
                    "840",
                    "292",
                    1752550659750
                ],
                [
                    "842",
                    "292",
                    1752550659766
                ],
                [
                    "844",
                    "291",
                    1752550659785
                ],
                [
                    "846",
                    "291",
                    1752550659800
                ],
                [
                    "848",
                    "291",
                    1752550659814
                ],
                [
                    "850",
                    "290",
                    1752550659831
                ],
                [
                    "852",
                    "290",
                    1752550659849
                ],
                [
                    "853",
                    "290",
                    1752550659866
                ],
                [
                    "854",
                    "289",
                    1752550659883
                ],
                [
                    "855",
                    "289",
                    1752550659901
                ],
                [
                    "855",
                    "289",
                    1752550659917
                ],
                [
                    "855",
                    "289",
                    1752550659949
                ],
                [
                    "856",
                    "289",
                    1752550659965
                ],
                [
                    "856",
                    "289",
                    1752550659987
                ],
                [
                    "857",
                    "289",
                    1752550659998
                ],
                [
                    "858",
                    "289",
                    1752550660020
                ],
                [
                    "859",
                    "289",
                    1752550660032
                ],
                [
                    "859",
                    "289",
                    1752550660049
                ],
                [
                    "860",
                    "289",
                    1752550660065
                ],
                [
                    "860",
                    "289",
                    1752550660084
                ],
                [
                    "861",
                    "289",
                    1752550660132
                ],
                [
                    "861",
                    "289",
                    1752550660317
                ],
                [
                    "860",
                    "289",
                    1752550660333
                ],
                [
                    "860",
                    "289",
                    1752550660334
                ]
            ],
            # Trajectory 2
            [
                [
                    "754",
                    "280",
                    1752550763584
                ],
                [
                    "787",
                    "304",
                    1752550763584
                ],
                [
                    "787",
                    "304",
                    1752550763781
                ],
                [
                    "789",
                    "304",
                    1752550763798
                ],
                [
                    "791",
                    "304",
                    1752550763815
                ],
                [
                    "796",
                    "304",
                    1752550763834
                ],
                [
                    "800",
                    "304",
                    1752550763848
                ],
                [
                    "804",
                    "304",
                    1752550763865
                ],
                [
                    "809",
                    "304",
                    1752550763882
                ],
                [
                    "814",
                    "304",
                    1752550763899
                ],
                [
                    "819",
                    "303",
                    1752550763915
                ],
                [
                    "824",
                    "303",
                    1752550763932
                ],
                [
                    "830",
                    "302",
                    1752550763949
                ],
                [
                    "835",
                    "302",
                    1752550763965
                ],
                [
                    "840",
                    "301",
                    1752550763982
                ],
                [
                    "845",
                    "301",
                    1752550764000
                ],
                [
                    "850",
                    "301",
                    1752550764017
                ],
                [
                    "854",
                    "300",
                    1752550764033
                ],
                [
                    "858",
                    "300",
                    1752550764050
                ],
                [
                    "861",
                    "300",
                    1752550764067
                ],
                [
                    "865",
                    "300",
                    1752550764083
                ],
                [
                    "869",
                    "300",
                    1752550764098
                ],
                [
                    "873",
                    "299",
                    1752550764114
                ],
                [
                    "877",
                    "299",
                    1752550764131
                ],
                [
                    "880",
                    "299",
                    1752550764148
                ],
                [
                    "882",
                    "299",
                    1752550764167
                ],
                [
                    "884",
                    "299",
                    1752550764182
                ],
                [
                    "886",
                    "299",
                    1752550764199
                ],
                [
                    "887",
                    "299",
                    1752550764217
                ],
                [
                    "889",
                    "299",
                    1752550764234
                ],
                [
                    "890",
                    "299",
                    1752550764250
                ],
                [
                    "891",
                    "299",
                    1752550764267
                ],
                [
                    "892",
                    "299",
                    1752550764283
                ],
                [
                    "893",
                    "299",
                    1752550764298
                ],
                [
                    "893",
                    "299",
                    1752550764314
                ],
                [
                    "893",
                    "299",
                    1752550764331
                ],
                [
                    "894",
                    "299",
                    1752550764381
                ],
                [
                    "894",
                    "299",
                    1752550764449
                ],
                [
                    "894",
                    "299",
                    1752550764532
                ],
                [
                    "894",
                    "299",
                    1752550764549
                ]
            ],
            # Trajectory 3
            [
                [
                    "754",
                    "280",
                    1752550806802
                ],
                [
                    "786",
                    "298",
                    1752550806802
                ],
                [
                    "786",
                    "298",
                    1752550806965
                ],
                [
                    "788",
                    "298",
                    1752550806982
                ],
                [
                    "795",
                    "298",
                    1752550807003
                ],
                [
                    "805",
                    "298",
                    1752550807017
                ],
                [
                    "818",
                    "298",
                    1752550807038
                ],
                [
                    "832",
                    "298",
                    1752550807050
                ],
                [
                    "845",
                    "298",
                    1752550807067
                ],
                [
                    "857",
                    "298",
                    1752550807083
                ],
                [
                    "870",
                    "298",
                    1752550807098
                ],
                [
                    "881",
                    "298",
                    1752550807116
                ],
                [
                    "890",
                    "298",
                    1752550807132
                ],
                [
                    "897",
                    "298",
                    1752550807150
                ],
                [
                    "903",
                    "298",
                    1752550807164
                ],
                [
                    "908",
                    "298",
                    1752550807182
                ],
                [
                    "912",
                    "298",
                    1752550807200
                ],
                [
                    "916",
                    "298",
                    1752550807218
                ],
                [
                    "919",
                    "297",
                    1752550807233
                ],
                [
                    "922",
                    "297",
                    1752550807252
                ],
                [
                    "925",
                    "297",
                    1752550807266
                ],
                [
                    "927",
                    "297",
                    1752550807282
                ],
                [
                    "929",
                    "297",
                    1752550807297
                ],
                [
                    "930",
                    "297",
                    1752550807314
                ],
                [
                    "931",
                    "297",
                    1752550807331
                ],
                [
                    "931",
                    "297",
                    1752550807348
                ],
                [
                    "932",
                    "297",
                    1752550807364
                ],
                [
                    "932",
                    "297",
                    1752550807399
                ],
                [
                    "932",
                    "297",
                    1752550807431
                ],
                [
                    "932",
                    "297",
                    1752550807447
                ],
                [
                    "933",
                    "297",
                    1752550807464
                ],
                [
                    "934",
                    "297",
                    1752550807481
                ],
                [
                    "934",
                    "297",
                    1752550807500
                ],
                [
                    "935",
                    "297",
                    1752550807514
                ],
                [
                    "936",
                    "297",
                    1752550807537
                ],
                [
                    "936",
                    "297",
                    1752550807599
                ],
                [
                    "936",
                    "297",
                    1752550807615
                ],
                [
                    "936",
                    "297",
                    1752550807648
                ],
                [
                    "937",
                    "297",
                    1752550807664
                ],
                [
                    "937",
                    "297",
                    1752550807682
                ],
                [
                    "937",
                    "297",
                    1752550807697
                ],
                [
                    "937",
                    "297",
                    1752550807716
                ],
                [
                    "938",
                    "297",
                    1752550807748
                ],
                [
                    "938",
                    "297",
                    1752550807767
                ],
                [
                    "938",
                    "297",
                    1752550807798
                ],
                [
                    "938",
                    "297",
                    1752550807815
                ],
                [
                    "938",
                    "296",
                    1752550807848
                ],
                [
                    "939",
                    "296",
                    1752550807881
                ],
                [
                    "939",
                    "296",
                    1752550807914
                ],
                [
                    "939",
                    "296",
                    1752550807947
                ],
                [
                    "939",
                    "296",
                    1752550807983
                ],
                [
                    "940",
                    "296",
                    1752550808015
                ],
                [
                    "940",
                    "296",
                    1752550808048
                ],
                [
                    "940",
                    "296",
                    1752550808082
                ],
                [
                    "940",
                    "296",
                    1752550808115
                ],
                [
                    "941",
                    "296",
                    1752550808131
                ],
                [
                    "941",
                    "296",
                    1752550808182
                ],
                [
                    "941",
                    "296",
                    1752550808198
                ],
                [
                    "941",
                    "296",
                    1752550808217
                ]
            ],
            # Trajectory 4
            [
                [
                    "754",
                    "280",
                    1752550859601
                ],
                [
                    "788",
                    "302",
                    1752550859601
                ],
                [
                    "788",
                    "302",
                    1752550859748
                ],
                [
                    "789",
                    "302",
                    1752550859764
                ],
                [
                    "792",
                    "302",
                    1752550859783
                ],
                [
                    "797",
                    "302",
                    1752550859811
                ],
                [
                    "802",
                    "302",
                    1752550859814
                ],
                [
                    "808",
                    "302",
                    1752550859835
                ],
                [
                    "816",
                    "302",
                    1752550859849
                ],
                [
                    "824",
                    "302",
                    1752550859867
                ],
                [
                    "833",
                    "302",
                    1752550859882
                ],
                [
                    "841",
                    "302",
                    1752550859898
                ],
                [
                    "849",
                    "302",
                    1752550859915
                ],
                [
                    "855",
                    "302",
                    1752550859932
                ],
                [
                    "861",
                    "302",
                    1752550859949
                ],
                [
                    "867",
                    "302",
                    1752550859966
                ],
                [
                    "872",
                    "302",
                    1752550859984
                ],
                [
                    "877",
                    "302",
                    1752550860001
                ],
                [
                    "883",
                    "302",
                    1752550860016
                ],
                [
                    "888",
                    "302",
                    1752550860033
                ],
                [
                    "892",
                    "302",
                    1752550860052
                ],
                [
                    "896",
                    "302",
                    1752550860067
                ],
                [
                    "899",
                    "302",
                    1752550860082
                ],
                [
                    "902",
                    "302",
                    1752550860098
                ],
                [
                    "906",
                    "302",
                    1752550860114
                ],
                [
                    "910",
                    "302",
                    1752550860131
                ],
                [
                    "913",
                    "302",
                    1752550860149
                ],
                [
                    "917",
                    "302",
                    1752550860166
                ],
                [
                    "921",
                    "302",
                    1752550860185
                ],
                [
                    "923",
                    "302",
                    1752550860200
                ],
                [
                    "926",
                    "302",
                    1752550860218
                ],
                [
                    "928",
                    "302",
                    1752550860233
                ],
                [
                    "931",
                    "302",
                    1752550860251
                ],
                [
                    "933",
                    "302",
                    1752550860266
                ],
                [
                    "936",
                    "302",
                    1752550860281
                ],
                [
                    "938",
                    "302",
                    1752550860298
                ],
                [
                    "941",
                    "301",
                    1752550860314
                ],
                [
                    "943",
                    "301",
                    1752550860331
                ],
                [
                    "945",
                    "301",
                    1752550860348
                ],
                [
                    "947",
                    "301",
                    1752550860365
                ],
                [
                    "949",
                    "300",
                    1752550860383
                ],
                [
                    "950",
                    "300",
                    1752550860400
                ],
                [
                    "951",
                    "300",
                    1752550860417
                ],
                [
                    "952",
                    "300",
                    1752550860433
                ],
                [
                    "952",
                    "300",
                    1752550860451
                ],
                [
                    "953",
                    "300",
                    1752550860481
                ],
                [
                    "953",
                    "300",
                    1752550860532
                ],
                [
                    "953",
                    "300",
                    1752550860548
                ],
                [
                    "953",
                    "300",
                    1752550860565
                ],
                [
                    "954",
                    "300",
                    1752550860582
                ],
                [
                    "954",
                    "300",
                    1752550860600
                ],
                [
                    "955",
                    "300",
                    1752550860614
                ],
                [
                    "957",
                    "299",
                    1752550860633
                ],
                [
                    "958",
                    "299",
                    1752550860650
                ],
                [
                    "958",
                    "299",
                    1752550860664
                ],
                [
                    "959",
                    "299",
                    1752550860681
                ],
                [
                    "959",
                    "299",
                    1752550860699
                ],
                [
                    "960",
                    "299",
                    1752550860764
                ],
                [
                    "959",
                    "299",
                    1752550860783
                ],
                [
                    "959",
                    "299",
                    1752550860801
                ]
            ]
        ]

        processed_templates = []
        for t in raw_templates:
            delta_track = self._preprocess_raw_template(t)
            displacement = np.sum(delta_track[:, :2], axis=0)
            distance = np.linalg.norm(displacement)
            processed_templates.append({
                'delta_track': delta_track,
                'total_displacement': displacement,
                'total_distance': distance
            })
        return processed_templates

    def _find_best_template(self):
        """遍历模板库，找到与目标距离最匹配的模板。"""
        min_diff = float('inf')
        best_template_data = None
        best_template_index = -1

        for i, template_data in enumerate(self.templates_data):
            diff = abs(template_data['total_distance'] - self.target_distance)
            if diff < min_diff:
                min_diff = diff
                best_template_data = template_data
                best_template_index = i

        return best_template_data, best_template_index

    def generate(self):
        """
        基于选中的最佳匹配模板，生成一条像素级精确的仿生轨迹。

        :return: list of [dx, dy, dt]
        """
        # 1. 提取最佳匹配模板的数据
        template_track = self.best_template['delta_track']
        template_displacement = self.best_template['total_displacement']

        # 2. 计算缩放比例
        scale = np.divide(self.target_xy, template_displacement,
                          out=np.ones_like(self.target_xy, dtype=float),
                          where=template_displacement != 0)

        # 3. 生成浮点数轨迹
        generated_track_float = []
        for dx_tpl, dy_tpl, dt_tpl in template_track:
            dx = dx_tpl * scale[0] + self.randomness * (random.random() - 0.5)
            dy = dy_tpl * scale[1] + self.randomness * (random.random() - 0.5)
            dt = dt_tpl + self.randomness * (random.random() - 0.5) * 5
            generated_track_float.append([dx, dy, max(1, dt)])

        # 4. 转换为整数并进行像素级精确修正
        generated_track_int = [[int(np.round(p[0])), int(np.round(p[1])), int(np.round(p[2]))] for p in
                               generated_track_float]

        current_displacement = np.sum(np.array(generated_track_int)[:, :2], axis=0)
        correction = self.target_xy - current_displacement

        num_points = len(generated_track_int)
        if num_points > 0:
            num_correction_points = min(15, num_points // 2)
            if num_correction_points > 0:
                start_index = num_points // 2 - num_correction_points // 2
                dx_corr_per_step = correction[0] / num_correction_points
                dy_corr_per_step = correction[1] / num_correction_points
                for i in range(num_correction_points):
                    generated_track_int[start_index + i][0] += dx_corr_per_step
                    generated_track_int[start_index + i][1] += dy_corr_per_step

            # 重新取整并应用最后的小数误差
            generated_track_int = [[int(np.round(p[0])), int(np.round(p[1])), p[2]] for p in generated_track_int]
            final_displacement = np.sum(np.array(generated_track_int)[:, :2], axis=0)
            final_correction = self.target_xy - final_displacement
            generated_track_int[-1][0] += int(final_correction[0])
            generated_track_int[-1][1] += int(final_correction[1])

        return generated_track_int


# --- 核心组件 4: 轨迹加密函数 ---
def string10to64(a):
    b = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-~')
    c = len(b)
    d = int(a)
    e = list()
    while True:
        mod = d % c
        d = d // c
        e.insert(0, b[mod])
        if not d:
            break
    return ''.join(e)


def prefixInteger(a, b):
    return str(a).zfill(b)


def pretreatment(a, b, c):
    e = string10to64(abs(a))
    f = str()
    if not c:
        f += '1' if a > 0 else '0'
    f += prefixInteger(e, b)
    return f


def getCoordinate(a):
    c = list()
    for d in range(len(a)):
        if d == 0:
            c.append(pretreatment(int(a[d][0]) if int(a[d][0]) < 0x3ffff else 0x3ffff, 3, True))
            c.append(pretreatment(int(a[d][1]) if int(a[d][1]) < 0xffffff else 0xffffff, 4, True))
            c.append(pretreatment(int(a[d][2]) if int(a[d][2]) < 0x3ffffffffff else 0x3ffffffffff, 7, True))
        else:
            e = int(a[d][0]) - int(a[d - 1][0])
            f = int(a[d][1]) - int(a[d - 1][1])
            g = int(a[d][2]) - int(a[d - 1][2])
            c.append(pretreatment(e if e < 0xfff else 0xfff, 2, False))
            c.append(pretreatment(f if f < 0xfff else 0xfff, 2, False))
            c.append(pretreatment(g if g < 0xffffff else 0xffffff, 4, True))
    return ''.join(c)


def base64_to_cv2_image(base64_string):
    """
    将Base64编码的字符串转换为OpenCV图像对象。
    自动处理 'data:image/png;base64,' 这样的前缀。
    """
    # 1. 检查并移除 'data:image/...' 前缀
    # 使用正则表达式以防格式略有不同
    if ',' in base64_string:
        base64_string = re.split(r'base64,', base64_string, maxsplit=1)[-1]

    # 2. 解码Base64字符串为二进制数据
    try:
        image_bytes = base64.b64decode(base64_string)
    except (base64.binascii.Error, ValueError) as e:
        print(f"Base64解码失败: {e}")
        return None

    # 3. 将二进制数据转换为NumPy数组
    image_array = np.frombuffer(image_bytes, np.uint8)

    # 4. 从NumPy数组解码为OpenCV图像
    # cv2.IMREAD_COLOR 会加载彩色图像
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    return image


def find_distance_from_base64(bg_base64, slider_base64, debug=False):
    """
    使用经过优化的边缘检测算法计算滑块距离，显著提高准确率。

    参数:
    bg_base64 (str): 带缺口的背景图的Base64编码。
    slider_base64 (str): 滑块图的Base64编码。

    返回:
    int: 优化后计算出的滑块需要移动的目标X坐标。
    """
    # 1. 解码Base64图像
    background_img = base64_to_cv2_image(bg_base64)
    slider_img = base64_to_cv2_image(slider_base64)

    if background_img is None or slider_img is None:
        return -1

    # --- 步骤A: 提纯滑块模板 ---
    # 提取滑块的Alpha通道作为掩码，如果没有alpha通道，则进行灰度二值化
    if slider_img.shape[2] == 4:  # 检查是否有Alpha通道
        # 使用Alpha通道作为掩码，这是最准确的方法
        slider_mask = slider_img[:, :, 3]
    else:
        # 如果没有Alpha通道，则通过灰度二值化创建掩码
        slider_gray = cv2.cvtColor(slider_img, cv2.COLOR_BGR2GRAY)
        # THRESH_BINARY_INV + THRESH_OTSU 可以很好地分离物体和背景
        _, slider_mask = cv2.threshold(slider_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # 对掩码进行Canny边缘检测，得到一个干净的滑块轮廓
    slider_edges = cv2.Canny(slider_mask, 100, 200)

    # --- 步骤B: 处理背景图像 ---
    # 将背景图转为灰度
    background_gray = cv2.cvtColor(background_img, cv2.COLOR_BGR2GRAY)
    # 高斯模糊降噪
    background_blurred = cv2.GaussianBlur(background_gray, (3, 3), 0)

    # 动态计算Canny的阈值，提高适应性
    median = np.median(background_blurred)
    lower_threshold = int(max(0, 0.7 * median))
    upper_threshold = int(min(255, 1.3 * median))
    background_edges = cv2.Canny(background_blurred, lower_threshold, upper_threshold)

    # --- 步骤C: 模板匹配与修正 ---
    result = cv2.matchTemplate(background_edges, slider_edges, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    target_x = max_loc[0]

    if debug:
        # --- 可视化调试 ---
        cv2.imshow('Clean Slider Edges (Template)', slider_edges)
        cv2.imshow('Background Edges (Search Space)', background_edges)

        # 在原始背景图上标记出最终位置
        slider_h, slider_w = slider_img.shape[:2]
        # 使用绿色矩形标记最终识别的位置
        cv2.rectangle(background_img, (target_x, max_loc[1]),
                      (target_x + slider_w, max_loc[1] + slider_h), (0, 255, 0), 2)
        # 使用红色小圆点标记原始匹配位置
        cv2.circle(background_img, (max_loc[0], max_loc[1]), 2, (0, 0, 255), -1)
        cv2.imshow('Final Result (Green=Final, Red=Original)', background_img)

        print("可视化窗口已显示。按任意键关闭...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # --- 可视化结束 ---

    return target_x


headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://passport.jd.com/uc/login",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
session = requests.Session()
session.headers.update(headers)

# 0. 初始化
response = session.get("https://passport.jd.com/uc/login")

# 1. 获取 _jdtdmap_sessionId
jdtdmap_session_id_url = "https://seq.jd.com/jseqf.html"
jdtdmap_session_id_params = {
    "bizId": "passport_jd_com_login_pc",
    "platform": "js",
    "version": "1"
}
jdtdmap_session_id_response = session.get(jdtdmap_session_id_url, params=jdtdmap_session_id_params)
jdtdmap_session_id = re.search('var _jdtdmap_sessionId="(.*?)";', jdtdmap_session_id_response.text).group(1)

# 2. 获取 token 和 eid
token = get_token(headers['user-agent'], "", "jd_pc_login", "passport.jd.com/uc/login")
eid = token[5:95]
session.cookies.update({
    "3AB9D23F7A4B3CSS": token,
    "3AB9D23F7A4B3C9B": eid,
})

# 3. 获取 publicKey
public_key_url = "https://passport.jd.com/publicKey/init"
public_key_response = session.get(public_key_url)
public_key = public_key_response.json()['data']

# 4. 获取 challenge
challenge_url = "https://iv.jd.com/slide/g.html"
challenge_params = {
    "appId": "1604ebb2287",
    "scene": "login",
    "product": "bind-suspend",
    "e": eid,
    "j": token,
    "lang": "zh_CN",
    "callback": "jsonp_047756609335558353"
}
challenge_response = session.get(challenge_url, params=challenge_params)
challenge_json = json.loads(re.search('jsonp_\d+\((.*?)\)', challenge_response.text).group(1))
challenge = challenge_json['challenge']

# 5. 计算鼠标轨迹
mouse_pos = [
    ["378", "367"], ["353", "369"], ["341", "371"], ["319", "374"], ["297", "376"], ["289", "378"], ["273", "381"],
    ["269", "381"], ["260", "382"], ["254", "384"], ["250", "384"], ["248", "384"], ["247", "385"], ["246", "385"],
    ["246", "385"], ["246", "385"], ["246", "385"], ["246", "385"], ["246", "386"], ["246", "386"], ["246", "386"],
    ["246", "386"], ["246", "387"], ["246", "387"], ["246", "387"], ["246", "387"], ["246", "388"], ["246", "389"],
    ["246", "389"], ["247", "389"], ["250", "390"], ["251", "391"], ["254", "393"], ["256", "395"], ["257", "397"],
    ["259", "399"], ["262", "404"], ["266", "408"], ["268", "411"], ["268", "412"], ["276", "442"], ["276", "442"],
    ["276", "446"], ["277", "450"], ["278", "453"], ["280", "458"], ["281", "463"], ["282", "468"], ["284", "473"],
    ["285", "478"], ["286", "483"], ["288", "488"], ["289", "492"], ["289", "494"], ["290", "498"], ["291", "501"],
    ["292", "504"], ["293", "507"], ["293", "509"], ["294", "511"], ["294", "513"], ["295", "515"], ["295", "516"],
    ["296", "517"], ["296", "517"], ["296", "518"], ["297", "518"], ["297", "519"], ["297", "519"], ["297", "519"],
    ["297", "519"], ["297", "520"], ["297", "520"], ["297", "520"]
]
timestamp = int(time.time() * 1000)
for i in range(len(mouse_pos)):
    mouse_pos[i][0] = str(int(mouse_pos[i][0]) + 500)
    mouse_pos[i].append(timestamp)
    timestamp += 8
d = getCoordinate(mouse_pos)

# 6. 第一次登录触发滑块
login_url = "https://iv.jd.com/slide/s.html"
login_params = {
    "d": d,
    "c": challenge,
    "w": "0",
    "appId": "1604ebb2287",
    "scene": "login",
    "product": "bind-suspend",
    "e": eid,
    "j": token,
    "s": jdtdmap_session_id,
    "o": "18935020391",
    "o1": "0",
    "u": "https://passport.jd.com/uc/login",
    "lang": "zh_CN",
    "callback": "jsonp_002426761280953027"
}
login_response = session.get(login_url, params=login_params)
login_json = json.loads(re.search('jsonp_\d+\((.*?)\)', login_response.text).group(1))
login_message = login_json['message']
login_next = login_json['nextVerify']

# 7. 获取滑块信息
slide_url = "https://iv.jd.com/slide/g.html"
slide_params = {
    "appId": "1604ebb2287",
    "scene": "login",
    "product": "click-bind-suspend",
    "e": eid,
    "j": token,
    "lang": "zh_CN",
    "callback": "jsonp_07829801017768782"
}
slide_response = session.get(slide_url, params=slide_params)
slide_json = json.loads(re.search('jsonp_\d+\((.*?)\)', slide_response.text).group(1))
slide_patch = slide_json['patch']
slide_bg = slide_json['bg']
slide_challenge = slide_json['challenge']
slide_y = slide_json['y']
slide_message = slide_json['message']
slide_o = slide_json['o']

# 8. 计算滑块距离
original_x = 754
original_y = 450
start_x = 785
start_y = 475

# 计算距离
target_distance = find_distance_from_base64(slide_bg, slide_patch)
# 生成轨迹

target_end_point = (target_distance, random.randint(-5, 5))
slider = HumanizedBestFitSlider(target_end_point)
generated_track = slider.generate()

slide_mouse_pos = list()
start_time = int(time.time() * 1000)
slide_mouse_pos.append([str(original_x), str(original_y), start_time])
slide_mouse_pos.append([str(start_x), str(start_y), start_time])

for point in generated_track:
    start_x += point[0]
    start_y += point[1]
    start_time += point[2]
    slide_mouse_pos.append([str(start_x), str(start_y), start_time])
time.sleep(float(slide_mouse_pos[-1][2] - slide_mouse_pos[0][2]) / 1000)

# 9. 验证滑块
check_url = "https://iv.jd.com/slide/s.html"
params = {
    "d": getCoordinate(slide_mouse_pos),
    "c": slide_challenge,
    "w": "342",
    "appId": "1604ebb2287",
    "scene": "login",
    "product": "click-bind-suspend",
    "e": eid,
    "j": token,
    "s": jdtdmap_session_id,
    "o": "18935020391",
    "o1": "0",
    "u": "https://passport.jd.com/uc/login",
    "lang": "zh_CN",
    "callback": "jsonp_009951571729723063"
}
check_response = session.get(check_url, params=params)
slide_json = json.loads(re.search('jsonp_\d+\((.*?)\)', check_response.text).group(1))
print(slide_json)

if slide_json['message'] == 'success':
    validate = slide_json['validate']
    print(validate)
