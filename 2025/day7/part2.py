#!/usr/bin/env python3

with open("input.txt", "r") as f:
    map = [line.strip() for line in f]
    start_col = map[0].find('S')
    beams = {(0, start_col): 1}
    total_timelines = 0
    height = len(map)
    width = len(map[0])
    while beams:
        new_beams = {}
        for (x, y), count in beams.items():
            if x >= height:
                total_timelines += count
                continue
            if map[x][y] == '^':
                if y - 1 >= 0:
                    new_beams[(x+1, y-1)] = new_beams.get((x+1, y-1), 0) + count
                if y + 1 < width:
                    new_beams[(x+1, y+1)] = new_beams.get((x+1, y+1), 0) + count
            else:
                new_beams[(x+1, y)] = new_beams.get((x+1, y), 0) + count
        beams = new_beams
    print(total_timelines)
