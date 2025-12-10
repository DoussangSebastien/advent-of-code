#!/usr/bin/env python3

from math import sqrt
from collections import Counter

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

# Calculate all distances
for i in range(len(boxes)):
    for j in range(i+1, len(boxes)):
        d = sqrt((boxes[i][0] - boxes[j][0])**2 + (boxes[i][1] - boxes[j][1])**2 + (boxes[i][2] - boxes[j][2])**2)
        distances_list.append((i, j, d))
sorted_distances = sorted(distances_list, key=lambda x: x[2])
parent = list(range(len(boxes)))
for box1, box2, dist in sorted_distances[:1000]:
    union_boxes(parent, box1, box2)
final_roots = [find_root(parent, i) for i in range(len(boxes))]
circuit_sizes = Counter(final_roots).values()
sorted_sizes = sorted(circuit_sizes, reverse=True)
print(sorted_sizes[0] * sorted_sizes[1] * sorted_sizes[2])
