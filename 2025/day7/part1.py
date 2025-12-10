#!/usr/bin/env python3

with open("input.txt", "r") as f:
    map = [line.strip() for line in f]
    beams = {(0, map[0].find('S'))}
    total_split = 0
    height = len(map)
    width = len(map[0])
    while beams:
        new_beams = set()
        for x, y in beams:
            if x >= height:
                continue
            if map[x][y] == '^':
                total_split += 1
                if y - 1 >= 0:
                    new_beams.add((x + 1, y - 1))
                if y + 1 < width:
                    new_beams.add((x + 1, y + 1))
            else:
                new_beams.add((x + 1, y))
        beams = new_beams
    print(total_split)
