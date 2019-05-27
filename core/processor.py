# -*- coding: utf-8 -*-

"""

"""

import cv2
import logging


logger = logging.getLogger(__name__)

sift = cv2.xfeatures2d.SIFT_create()

FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

def build_features(img_path):
    """构建图像特征"""

    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kp, des = sift.detectAndCompute(gray, None)

    return des


def match(des_a, des_b):
    """计算两组特征的相似程度"""

    count = 0
    matches = flann.knnMatch(des_a, des_b, k=2)
    for m, n in matches:
        if m.distance < 0.50 * n.distance:
            count = count + 1

    return count

