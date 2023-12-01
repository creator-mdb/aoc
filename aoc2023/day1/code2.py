#!/usr/bin/env python
# coding: utf-8
"""
AoC 2023 day 1 - Solution 2/2
"""

mapping_table = {
    'one':      '1', 
    'two':      '2', 
    'three':    '3', 
    'four':     '4', 
    'five':     '5', 
    'six':      '6', 
    'seven':    '7', 
    'eight':    '8', 
    'nine':     '9'
}

def parse(chunk):
    """
    Parse the given chunk based on the mapping table.

    Parameters:
    - chunk (str): The input string to be parsed.

    Returns:
    - str or None: The matched key from the mapping table or None if no match is found.
    """
    for item in mapping_table.items():
        if chunk.startswith(item[0]):
            return item[0]
    return None

tot = 0 # pylint: disable=invalid-name
with open("aoc2023/day1/input.txt", encoding="utf-8") as file:
    for line in file:
        line = line.replace("\n", "")
        line_len = len(line)
        start_at = 0 # pylint: disable=invalid-name
        number = '' # pylint: disable=invalid-name
        while start_at < line_len:
            if line[start_at].isdigit():
                number += line[start_at]
                start_at += 1
            else:
                key = parse(line[start_at:])
                if key is not None:
                    number += mapping_table[key]
                    start_at += len(key) - 1
                else:
                    start_at += 1

        tot += int(number[0] + number[len(number) - 1])
print(tot)
