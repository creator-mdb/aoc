#!/usr/bin/env python
# coding: utf-8

"""
AoC 2023 day 3 - Solution 1/2
"""

import re

def scan_line(line, regex):
    """
    Scans a given line using a regular expression pattern and returns a list of dictionaries
    containing information about each match found.

    Parameters:
    - line (str): The input line to be scanned for matches.
    - regex (str): The regular expression pattern used for matching.

    Returns:
    List[dict]: A list of dictionaries, where each dictionary represents a match found in the line.
                Each dictionary contains the following key-value pairs:
                - 'item': The matched substring.
                - 'start': The starting index of the matched substring in the input line.
                - 'end': The ending index (exclusive) of the matched substring in the input line.
    """
    items_v = []
    items = re.compile(regex)
    matches = items.finditer(line)
    for match in matches:
        items_v.append({ 'item': match.group(),'start': match.start(), 'end': match.end() })

    return items_v

def load_file(file_name):
    """
    Reads a text file and extracts numeric values and symbols from each line.

    Parameters:
    - file_name (str): The name of the file to be loaded.

    Returns:
    Tuple[List[List[Dict[str, Union[str, int]]]], List[List[Dict[str, Union[str, int]]]]]:
        A tuple containing two lists:
        1. List of dictionaries representing numeric values found in each line.
        2. List of dictionaries representing non-numeric symbols found in each line.

        Each dictionary in the lists contains the following key-value pairs:
        - 'item': The matched substring.
        - 'start': The starting index of the matched substring in the line.
        - 'end': The ending index (exclusive) of the matched substring in the line.
        - 'line_number': The line number in the file.
    """
    line_counter = 0
    with open(file_name, encoding="utf-8") as file:
        numbers_v = []
        symbols_v = []
        for line in file:
            line = line.replace("\n", "")

            numbers_v.append([line_counter])
            # Extract numbers
            numbers_v[line_counter] = scan_line(line, r'\d+')

            symbols_v.append([line_counter])
            # Extract symbols
            symbols_v[line_counter] = scan_line(line, r"[^\d\.]")

            line_counter += 1
    return (numbers_v, symbols_v)

def check_number_symbols_in_line(number, symbols_v, line):
    """
    Checks if a given number and symbol in a line ßoverlap or are adjacent.

    Parameters:
    - number (dict): A dictionary representing information about a numeric value.
                     Should contain keys 'start' and 'end' representing the start and end indices.
    - symbol (dict): A dictionary representing information about a symbol.
                     Should contain keys 'start' and 'end' representing the start and end indices.
    - line (int): The line number in which the check is performed.

    Returns:
    bool: True if the number and symbol overlap or are adjacent, False otherwise.
    """
    for symbol in symbols_v[line]:
        # Check number on the left of the symbol
        if symbol['start'] <= number['start'] <= symbol['end']:
            return True
        # Check number on the right of the symbol
        if symbol['start'] <= number['end'] <= symbol['end']:
            return True
        # Check symbol in the middle of the number
        if number['start'] <= symbol['start'] <= number['end']: # and (two lines 'cause linter E501)
            if number['start'] <= symbol['end'] <= number['end']:
                return True
    return False

def pick_numbers(numbers_v, symbols_v):
    """
    Picks numeric values that have a specific relationship 
    with symbols in adjacent lines or in the same line.

    Parameters:
    - numbers_v (List[List[Dict[str, Union[str, int]]]]): 
      A list of lists of dictionaries representing numeric values
      in each line. Each dictionary should contain keys 'item',
      'start', 'end', and 'line_number'.
    - symbols_v (List[List[Dict[str, Union[str, int]]]]): 
      A list of lists of dictionaries representing symbols
      in each line. Each dictionary should contain keys 'item',
      'start', 'end', and 'line_number'.

    Returns:
    List[int]: A list of selected numeric values based on their relationship 
    with symbols in adjacent lines or in the same line.
    """
    results = []
    lines = len(numbers_v)
    for line in range(0, lines):
        for number in numbers_v[line]:
            # Check number against same line
            for symbol in symbols_v[line]:
                if number['start'] == symbol['end'] or number['end'] == symbol['start']:
                    results.append(int(number['item']))
                    break
            # Check number against lower line
            if line + 1 < lines:
                if check_number_symbols_in_line(number, symbols_v, line + 1):
                    results.append(int(number['item']))
            # Check number against upper line
            if line - 1 >= 0:
                if check_number_symbols_in_line(number, symbols_v, line - 1):
                    results.append(int(number['item']))
    return results

def main():
    """
    Reads data from a file using the load_file function, picks numbers based on their
    relationship with symbols using the pick_numbers function, and prints the selected
    numbers and their sum.
    """
    (numbers_v, symbols_v) = load_file("aoc2023/day3/input.txt")
    numbers = pick_numbers(numbers_v, symbols_v)
    print(numbers)
    print(sum(numbers))

# Check if the script is being run as the main module
if __name__ == "__main__":
    main()
