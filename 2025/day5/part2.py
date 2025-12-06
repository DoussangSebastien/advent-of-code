#!/usr/bin/env python3

with open("input.txt") as f:
    lines = [line.strip() for line in f]
    range_lines = lines[:lines.index("")]
    intervals = []
    merged = []
    total = 0
    for line in range_lines:
        interval = line.split("-")
        start, end = int(interval[0]), int(interval[1])
        intervals.append((start, end))
    intervals.sort()
    cur_start, cur_end = intervals[0]
    for start, end in intervals[1:]:
        if start <= cur_end + 1:
            cur_end = max(cur_end, end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end
    merged.append((cur_start, cur_end))
    for start, end in merged:
        total += (end - start + 1)

    print(total)
