#!/usr/bin/env python3

from math import sqrt

def find_root(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find_root(parent, parent[i]) 
    return parent[i]

def union_boxes(parent, i, j):
    root_i = find_root(parent, i)
    root_j = find_root(parent, j)
    if root_i != root_j:
        parent[root_i] = root_j
        return True
    return False

with open("input.txt", "r") as f:
    boxes = [[int(x) for x in line.strip().split(",")] for line in f]
    distances_list = []
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            d = sqrt((boxes[i][0] - boxes[j][0])**2 + (boxes[i][1] - boxes[j][1])**2 + (boxes[i][2] - boxes[j][2])**2)
            distances_list.append((i, j, d))
    sorted_distances = sorted(distances_list, key=lambda x: x[2])
    parent = list(range(len(boxes)))
    num_groups = len(boxes)
    for box1_idx, box2_idx, dist in sorted_distances:
        if union_boxes(parent, box1_idx, box2_idx):
            num_groups -= 1
            if num_groups == 1:
                print(boxes[box1_idx][0] * boxes[box2_idx][0])
                break
