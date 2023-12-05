#!/usr/bin/env python
# coding: utf-8

"""
AoC 2023 day 4 - Solution 2/2
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
        items_v.append(match.group())

    return items_v

def load_file(file_name):
    """
    Reads a text file and extracts numeric values and symbols from each line.

    Parameters:
    - file_name (str): The name of the file to be loaded.

    Returns:
    List[Dict[str, Union[int, List[int]]]]:
        A list of dictionaries representing information extracted from each line.
        Each dictionary contains the following key-value pairs:
        - 'card_id' (int): The card number extracted from the line.
        - 'mynumbers' (List[int]): Numeric values extracted from the 'mynumbers' section.
        - 'winning' (List[int]): Numeric values extracted from the 'winning_numbers' section.

    Notes:
        - The input file is expected to have lines formatted as 
          'card_number:winning_numbers|mynumbers'.
    """
    with open(file_name, encoding="utf-8") as file:
        cards = []
        for line in file:
            line = line.replace("\n", "")

            (card, all_numbers) = line.split(":", 2)
            card_number = int(scan_line(card, r'\d+')[0])
            (winning_numbers, mynumbers) = all_numbers.split("|", 2)

            newcard = { 'card_id': card_number }

            # Extract mynumbers
            newcard['mynumbers'] = scan_line(mynumbers, r'\d+')

            # Extract winnin numbers
            newcard['winning'] = scan_line(winning_numbers, r'\d+')

            cards.append(newcard)

    return cards

def check_winning_numbers(card):
    """
    Identify winning numbers on a player card.

    Parameters:
    - card (dict): A dictionary representing a player card, 
      containing 'mynumbers' and 'winning' lists.

    Returns:
    list: A list containing the winning numbers present on the player card.

    Note:
    The function iterates through the 'mynumbers' on the player card and checks for matches
    with the 'winning' numbers. If a match is found, the winning number is added to the list.
    """
    winning_numbers = []

    for mynumber in card['mynumbers']:
        for winning in card['winning']:
            if mynumber == winning:
                winning_numbers.append(winning)
                break
    return winning_numbers

def pick_winning_cards(cards):
    """
    Identify winning numbers from a list of cards.

    Parameters:
    - cards (list): A list of cards, where each card is a 
      dictionary with a 'card_id' and a list of numbers.

    Returns:
    list: A list containing dictionaries for each winning card in the input list.
          Each dictionary includes 'card_id' and 'numbers', where 'numbers' are 
          determined by the `check_winning_numbers` function.
    """
    results = []
    for card in cards:
        winning_numbers = check_winning_numbers(card)
        if winning_numbers:
            new_winning_card = { 'card_id': card['card_id'], 'numbers': winning_numbers }
            results.append(new_winning_card)
    return results

def process_cards(cards, winning_cards):
    """
    Calculate the score based on the interaction between player cards and winning cards.

    Parameters:
    - cards (list): A list of player cards, where each card is a dictionary 
      with a 'card_id' and a list of numbers.
    - winning_cards (list): A list of winning cards, where each card 
      is a dictionary with a 'card_id' and 'numbers'.

    Returns:
    int: The total score calculated based on the interaction between player cards and winning cards.

    Note:
    The function recursively processes the cards and winning cards to calculate the score. 
    It considers the number of matching numbers between player cards and winning cards. 
    The score is incremented for each matched number, and the function recursively processes 
    newly won cards using the `pick_winning_cards` function.
    """
    score = 0
    for winning_card in winning_cards:
        win_cnt = len(winning_card['numbers'])
        cards_won = []
        for card_id in range(winning_card['card_id'] + 1, winning_card['card_id'] + win_cnt + 1):
            cards_won.append(cards[card_id - 1])
        score += len(cards_won) + process_cards(cards, pick_winning_cards(cards_won))
    return score

def main():
    """
    A script to process player cards, determine winning numbers,
    and calculate points based on the correspondences.

    Reads player cards from a file using the load_file function, picks winning 
    numbers based on their correspondences using the pick_winning_cards function, 
    and prints the total points calculated based on the number of winning numbers.
    """
    cards = load_file("aoc2023/day4/input.txt")
    print(len(cards) + process_cards(cards, pick_winning_cards(cards)))

# Check if the script is being run as the main module
if __name__ == "__main__":
    main()
