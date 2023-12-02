#!/usr/bin/env python
# coding: utf-8
"""
AoC 2023 day 2 - Solution 2/2
"""

tot = 0 # pylint: disable=invalid-name

def parse(content):
    """
    Parses a string containing color quantity information and returns the maximum quantity
    for each of the three primary colors: red, green, and blue.

    Parameters:
    - content (str): A string containing color quantity information separated by semicolons
                    and color-quantity pairs separated by commas. Each pair consists of a
                    quantity and a color name.

    Returns:
    tuple: A tuple containing the maximum quantity for red, green, and blue colors, respectively.

    Example:
    >>> parse("2 red, 5 green; 3 red, 7 blue; 1 green, 4 blue")
    (3, 7, 4)

    Note:
    - The function assumes a specific format for the input string, where colors are named
      ('red', 'green', 'blue') and quantities are integers.
    - If the input format does not adhere to the expected structure, the function behavior
      may not be accurate.
    """
    color_max = { 'red': 0, 'green': 0, 'blue': 0 }
    grabs = content.split(';')
    for grab in grabs:
        subsets = grab.split(',')
        for subset in subsets:
            subset = subset.strip()
            (qty, color) = subset.split(' ', 2)
            if color_max[color] < int(qty):
                color_max[color] = int(qty)
    return (color_max['red'], color_max['green'], color_max['blue'])

with open("aoc2023/day2/input.txt", encoding="utf-8") as file:
    for line in file:
        line = line.replace("\n", "")
        contents = line.split(':')
        (red, green, blue) = parse(contents[1].strip())
        tot += red * green * blue
print(tot)
