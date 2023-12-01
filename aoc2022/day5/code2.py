import re

def main():
    # Manual parsing... pragmatic approach... when data entry is faster than coding :)
    stacks = []
    stacks.append(['Q', 'M', 'G', 'C', 'L'])
    stacks.append(['R', 'D', 'L', 'C', 'T', 'F', 'H', 'G'])
    stacks.append(['V', 'J', 'F', 'N', 'M', 'T', 'W', 'R'])
    stacks.append(['J', 'F', 'D', 'V', 'Q', 'P'])
    stacks.append(['N', 'F', 'M', 'S', 'L', 'B', 'T'])
    stacks.append(['R', 'N', 'V', 'H', 'C', 'D', 'P'])
    stacks.append(['H', 'C', 'T'])
    stacks.append(['G', 'S', 'J', 'V', 'Z', 'N', 'H', 'P'])
    stacks.append(['Z', 'F', 'H', 'G'])

    priority = 0
    with open("day5/input2.txt") as file:
        lines = file.readlines()

    for line in lines:
        line = line.replace("\n", "")
        (qty, stackFrom, stackTo) = re.findall("\d+", line)
        crateStack = []
        for x in range(int(qty)):
            crateStack.append(stacks[int(stackFrom)-1].pop())
        for x in range(int(qty)):
            stacks[int(stackTo)-1].append(crateStack.pop())

    for stack in stacks:
        print(stack.pop())

if __name__ == "__main__":
    main()
