def rangestr2set(rangestr):
    a, b = rangestr.split('-')
    a, b = int(a), int(b)
    result = range(a, b + 1)
    return set(result)

def main():
    overlapping = 0
    with open("day4/input.txt") as file:
        for line in file:  
            pairs = line.replace("\n", "").split(",")
            set1 = rangestr2set(pairs[0])
            set2 = rangestr2set(pairs[1])
            intersection = set1 & set2
            if intersection != set():
                overlapping += 1
    print(overlapping)

if __name__ == "__main__":
    main()
