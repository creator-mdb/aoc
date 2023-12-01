#!/usr/bin/env python
# coding: utf-8
"""
AoC 2023 day 1 - Solution 1/2
"""
import re

tot = 0 # pylint: disable=invalid-name
with open("aoc2023/day1/input.txt", encoding="utf-8") as file:
    for line in file:
        all_digits_captured = re.findall(r"(\d)", line)
        digits_str = ''.join(all_digits_captured) # pylint: disable=invalid-name
        number = int(digits_str[0] + digits_str[len(digits_str) - 1])
        tot += number
print(tot)
