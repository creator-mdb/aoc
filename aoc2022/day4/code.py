def rangestr2set(rangestr):
    a, b = map(int, rangestr.split('-'))
    return set(range(a, b + 1))

def main():
    fullyContained = 0
    with open("day4/input.txt") as file:
        for line in file:  
            pairs = line.replace("\n", "").split(",")
            set1 = rangestr2set(pairs[0])
            set2 = rangestr2set(pairs[1])
            intersection = set1 & set2
            if intersection == set1 or intersection == set2:
                fullyContained += 1
    print(fullyContained)

if __name__ == "__main__":
    main()
