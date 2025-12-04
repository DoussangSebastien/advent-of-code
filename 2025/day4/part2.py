#!/usr/bin/env python3

def check_row(paper_map, x, y, row_size, num_col):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= row_size and 0 <= ny <= num_col:
            if paper_map[ny][nx] == '@':
                count += 1
    return count

def check_movable(paper_map, x, y, row_size, num_col, count):
    if paper_map[y][x] == '@':
        surrounding_count = check_row(paper_map, x, y, row_size, num_col)
        if surrounding_count < 4:
            paper_map[y] = paper_map[y][:x] + 'x' + paper_map[y][x + 1:] #could use it for part two :)
            count += 1
    return count

with open("input.txt", "r") as f:
    paper_map = [line.strip() for line in f]
    row_size = len(paper_map[0]) - 1
    num_col = len(paper_map) - 1
    count = 0
    for _ in range(num_col + 1):
        for y in range(num_col + 1):
            for x in range(row_size + 1):
                count = check_movable(paper_map, x, y, row_size, num_col, count)
    print(count)
