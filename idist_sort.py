"""
handle iDist ordering
"""
# !/usr/bin/env python
# coding=utf-8

QI_LEN = 7
CENTERS = 1024
ids = {}


def _2Dist(data, i, j):
    dist = 0.0
    for dim in range(QI_LEN):
        dist += (data[i][dim] - data[j][dim]) ** 2
    return sqrt(dist)


def Gonzalez(data, data_size, ref_points):
    """
    """
    data_size = len(data)
    centers = []
    dist = [1000000] * data_size
    nei = []
    centers[0] = 0
    dist[0] = 0
    ne[0] = 0

    for i in range(1, data_size):
        dist[i] = _2Dist(data, 0, i)
        nei[i] = 0

    max_dis = -1000000
    max_index = -1
    for k in range(1, CENTERS + 1):
        max_dis = 0
        for i in range(1, data_size):
            try:
                if ids[i] > max_dis:
                    max_dis = dist[i]
                    max_index = i
            except KeyError:
                continue
        centers[k] = max_index
        ids[max_index] = max_index
        dist[max_index] = 0
        if k == 1:
            for i in range(data_size):
                temp = _2Dist(data, max_index, i)
                if temp < dist[i]:
                    nei[i] = max_index
                    dist[i] = temp
    s = []
    for i in range(CENTERS):
        for j in range(QI_LEN):
            ref_points = data[centers[i + 1]]


def determine_order(data, n, sample, sample_size):
    ref_points = []
    for i in range(CENTERS):
        ref_points[i] = []
    Gonzalez(sample, sample_size, ref_points)
    hbt_sort_arrary(ref_points, CENTERS, true)

    coords = []
    for rec in range(n):
        for j in range(QI_LEN):
            coords[j] = (data[rec][j] - domanin_start[j]) / domanin_length[j]
        int mindistnum = -1
        mindist = 1e10
        dist = 0
        temp = 0

        for i in range(CENTERS):
            dist = 0
            for j in range(QI_LEN):
                temp = coords[j] - ref_points[i][j]
                dist += temp ** 2
            if dist < mindist:
                mindist = dist
                mindistnum = i

        data[rec].tmp_sort_value = 1e6 * (QI_LEN * mindistnum + sqrt(mindist))
