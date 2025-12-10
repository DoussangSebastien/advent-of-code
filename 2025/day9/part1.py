#!/usr/bin/env python3

from math import inf

with open("input.txt", "r") as f:
    coords = [[int(x) for x in line.strip().split(",")] for line in f]
    size = len(coords)
    max_area = -inf
    for i in range(size):
        for j in range(size):
            width = abs(coords[j][0] - coords[i][0]) + 1
            height = abs(coords[j][1] - coords[i][1]) + 1
            area = width * height
            if area > max_area:
                max_area = area
    print(max_area)
