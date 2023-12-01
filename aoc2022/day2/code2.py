#!/usr/bin/env python
# coding: utf-8

# A X = 3 + 0 = 3
# A Y = 1 + 3 = 4
# A Z = 2 + 6 = 8
# B X = 1 + 0 = 1
# B Y = 2 + 3 = 5
# B Z = 3 + 6 = 9
# C X = 2 + 0 = 2
# C Y = 3 + 3 = 6
# C Z = 1 + 6 = 7

score = 0
file = open("day2/input.txt")
for line in file:  
    strategy = line.replace("\n", "")
    match strategy:
        case "A X": 
            score += 3
        case "A Y":
            score += 4
        case "A Z":
            score += 8
        case "B X":
            score += 1
        case "B Y":
            score += 5
        case "B Z":
            score += 9
        case "C X":
            score += 2
        case "C Y":
            score += 6
        case "C Z":
            score += 7
        case _:
            print("Line skipped: '" + strategy)
file.close()
print(score)
