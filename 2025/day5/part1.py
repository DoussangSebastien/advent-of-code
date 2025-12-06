#!/usr/bin/env python3

with open("input.txt", "r") as f:
    content = [block.split("\n") for block in f.read().strip().split("\n\n")]
    ids = content[0]
    ingredients = content[1]
    count = 0
    for ingredient in ingredients:
        for id in ids:
            interval = id.split("-")
            if int(interval[0]) <= int(ingredient) <= int(interval[1]):
                count += 1
                break
    print(count)
