def calcPriority(item):
    # 1-26 priorities for lowercase, otherwise 27-52 priorities
    # 97 is 'a' ASCII decimal value
    # 65 is 'A' ASCII decimal value 
    return ord(item) + 1 - 97 if item.islower() else ord(item) + 27 - 65

def main():
    priority = 0
    with open("day3/input.txt") as file:
        for line in file:
            line_len = len(line) - 1
            # Cycle first half
            for x in range(0, int(line_len / 2)):
                # Cycle second half
                for y in range(int(line_len / 2), line_len):
                    if line[x] == line[y]:
                        priority += calcPriority(line[x])
                        break
                    else:
                        continue
                break
            else:
                print("Duplicate item not found on line: " + line)
        print(priority)

if __name__ == "__main__":
    main()