#!/usr/bin/env python3

def find_biggest_j(battery):
    size = 12
    current_index = 0
    result = ""
    while size > 0:
        search_end = len(battery) - size + 1
        interval = battery[current_index:search_end]
        max_digit = max(interval)
        relative_index = interval.index(max_digit)
        result += max_digit
        current_index += relative_index + 1
        size -= 1
    return result

with open("input.txt", "r") as f:
    total_j = 0
    for line in f:
        total_j += int(find_biggest_j(line.strip()))
    print(total_j)
