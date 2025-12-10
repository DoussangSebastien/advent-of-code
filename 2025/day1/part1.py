#!/usr/bin/env python3

def rotate_right(value, rot_value):
    return (value + int(rot_value)) % 100

def rotate_left(value, rot_value):
    return (value - int(rot_value)) % 100

def rotate(cur_value, line):
    if line[0] == 'L':
        return rotate_left(cur_value, line[1::])
    return rotate_right(cur_value, line[1::])

with open("input.txt", "r") as f:
    count = 0
    cur_value = 50
    for line in f:
        cur_value = rotate(cur_value, line)
        if cur_value == 0:
            count += 1

    print(count)
