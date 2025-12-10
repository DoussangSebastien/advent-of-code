#!/usr/bin/env python3

from math import inf

def get_edges(coords):
    edges = []
    num = len(coords)
    for i in range(num):
        p1 = coords[i]
        p2 = coords[(i + 1) % num]
        edges.append((p1, p2))
    return edges

def is_valid_rectangle(p1, p2, edges):
    rx_min = min(p1[0], p2[0])
    rx_max = max(p1[0], p2[0])
    ry_min = min(p1[1], p2[1])
    ry_max = max(p1[1], p2[1])
    for edge_start, edge_end in edges:
        if edge_start[0] == edge_end[0]:
            ex = edge_start[0]
            ey_low, ey_high = sorted((edge_start[1], edge_end[1]))
            if rx_min < ex < rx_max:
                if max(ry_min, ey_low) < min(ry_max, ey_high):
                    return False
        else:
            ey = edge_start[1]
            ex_low, ex_high = sorted((edge_start[0], edge_end[0]))
            if ry_min < ey < ry_max:
                if max(rx_min, ex_low) < min(rx_max, ex_high):
                    return False
    cx = (rx_min + rx_max) / 2
    cy = (ry_min + ry_max) / 2
    intersections = 0
    for edge_start, edge_end in edges:
        if edge_start[0] == edge_end[0]: 
            ex = edge_start[0]
            ey_low, ey_high = sorted((edge_start[1], edge_end[1]))
            if ex > cx and ey_low < cy < ey_high:
                intersections += 1
    if intersections % 2 == 0:
        return False
    return True

with open("input.txt", "r") as f:
    coords = [[int(x) for x in line.strip().split(",")] for line in f]
    edges = get_edges(coords)
    size = len(coords)
    max_area = -inf
    for i in range(size):
        for j in range(size):
            width = abs(coords[j][0] - coords[i][0]) + 1
            height = abs(coords[j][1] - coords[i][1]) + 1
            area = width * height
            if area > max_area:
                if is_valid_rectangle(coords[i], coords[j], edges):
                    max_area = area
    print(max_area)
