#!/usr/bin/env python3

def check_id_value(id):
    if len(id) % 2 != 0:
        return False
    size = len(id) // 2
    return id[:size] == id[size:]

with open("input.txt", "r") as f:
    final_id = 0
    ids = f.read().strip().split(",")
    for id_range in ids:
        start, end = id_range.split("-")
        start, end = int(start), int(end)
        for i in range(start, end + 1):
            if check_id_value(str(i)):
                final_id += i
    print(final_id)
