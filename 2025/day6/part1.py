#!/usr/bin/env python3

with open("input.txt", "r") as f:
    maths = [line.strip().split() for line in f]
    maths_size = len(maths) - 1
    lenght = len(maths[0])
    total = 0

    for i in range(lenght):
        if maths[maths_size][i] == '+':
            current = 0
            for j in range(maths_size):
                current += int(maths[j][i])
        else:
            current = 1
            for j in range(maths_size):
                current *= int(maths[j][i])
        total += current

    print(total)
