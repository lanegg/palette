# -*- coding: utf-8 -*-

"""

"""

import cv2
import logging
import core.utils as utils
import core.library as lib


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


def scan():
    """查找对应专辑"""
    source_des = build_features(utils.config["debug_photo_path"])
    match_album = None
    result_count = 0

    for album_path in lib.library.albums.keys():
        count = match(lib.library.albums[album_path].features, source_des)
        if count > result_count:
            result_count = count
            match_album = album_path

    return lib.library.albums[match_album]
