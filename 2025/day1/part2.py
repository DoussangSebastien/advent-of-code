#!/usr/bin/env python3

def rotate_right(value, rot_value):
    steps = int(rot_value)
    hits = 0
    for _ in range(steps):
        value = (value + 1) % 100
        if value == 0:
            hits += 1
    return value, hits


def rotate_left(value, rot_value):
    steps = int(rot_value)
    hits = 0
    for _ in range(steps):
        value = (value - 1) % 100
        if value == 0:
            hits += 1
    return value, hits


def rotate(cur_value, line):
    if line[0] == 'L':
        return rotate_left(cur_value, line[1::])
    return rotate_right(cur_value, line[1::])


with open("input.txt", "r") as f:
    total_hits = 0
    cur_value = 50
    for line in f:
        cur_value, hits = rotate(cur_value, line)
        total_hits += hits

    print(total_hits)
