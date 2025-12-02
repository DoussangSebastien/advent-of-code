#!/usr/bin/env python3

def check_id_value(id):
    if len(id) % 2 != 0:
        return False
    size = len(id) // 2
    return id[:size] == id[size:]

def check_id_pattern(id):
    size = len(id)
    for i in range(1, size // 2 + 1):
        if size % i == 0:
            pattern = id[:i]
            if pattern * (size // i) == id:
                return True
    return False

with open("input.txt", "r") as f:
    final_id = 0
    ids = f.read().strip().split(",")
    for id_range in ids:
        start, end = id_range.split("-")
        start, end = int(start), int(end)
        for i in range(start, end + 1):
            if check_id_value(str(i)):
                final_id += i
                continue
            if check_id_pattern(str(i)):
                final_id += i # was adding 1 instead of i and spent way too much time finding that
    print(final_id)
