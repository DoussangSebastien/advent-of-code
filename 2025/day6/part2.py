#!/usr/bin/env python3

def calculate(numbers, operator):
    res = numbers[0]
    for num in numbers[1:]:
        if operator == '+':
            res += num
        elif operator == '*':
            res *= num
    return res

with open("input.txt", "r") as f:
    raw_lines = [line.strip('\n') for line in f]
    max_width = max(len(line) for line in raw_lines)
    grid = [line.ljust(max_width) for line in raw_lines]
    number_rows = grid[:-1]
    operator_row = grid[-1]
    total_global = 0
    current_numbers = [] 
    current_operator = None 
    for x in range(max_width):
        col_chars = [row[x] for row in number_rows]
        is_separator = all(c == ' ' for c in col_chars)
        if not is_separator:
            number_str = "".join(col_chars).replace(' ', '')
            if number_str:
                current_numbers.append(int(number_str))
            op_char = operator_row[x]
            if op_char in ['+', '*']:
                current_operator = op_char
        else:
            if current_numbers:
                res = calculate(current_numbers, current_operator)
                total_global += res
                current_numbers = []
                current_operator = None
    if current_numbers:
        res = calculate(current_numbers, current_operator)
        total_global += res
    print(total_global)
