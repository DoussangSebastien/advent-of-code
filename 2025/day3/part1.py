#!/usr/bin/env python3

def find_biggest_j(battery):
    index_max = max(range(len(battery) - 1), key=battery.__getitem__)
    end = battery[index_max + 1:]
    return battery[index_max] + max(end)

with open("input.txt", "r") as f:
    total_j = 0
    for line in f:
        total_j += int(find_biggest_j(line.strip()))
    print(total_j)
