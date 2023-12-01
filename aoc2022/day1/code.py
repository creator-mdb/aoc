#!/usr/bin/env python
# coding: utf-8

bags = [0]
with open("day1/input.txt") as file:
    for line in file:
        if line == '\n':
            bags.append(0)
        else:
            bags[-1] += int(line)
bags.sort()
print(bags)
