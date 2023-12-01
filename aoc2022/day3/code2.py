def calcPriority(item):
    # 1-26 priorities for lowercase, otherwise 27-52 priorities
    # 97 is 'a' ASCII decimal value
    # 65 is 'A' ASCII decimal value 
    return ord(item) + 1 - 97 if item.islower() else ord(item) + 27 - 65

def findSameItems(rucksackA, rucksackB):
    return set(filter(lambda x: x in rucksackA, rucksackB))
#    same = set()
#    for itemA in rucksackA:
#        for itemB in rucksackB:
#            if itemA == itemB: 
#                same.add(itemA)
#    return same

def main():
    priority = 0
    file = open("day3/input.txt")

    while 1: # Read all groups
        members = []
        for x in range (1,4):
            line = file.readline()
            if len(line) == 0: # EOF
                if x != 1:
                    print("Premature end of group! Stopped at member n° " | x)
                file.close()
                print(priority)
                quit()
            members.append(line.replace("\n", ""))

        # Check first two members
        sameItems = findSameItems(members[0], members[1])
        if sameItems == []:
            print("Cannot find one single same item on first two members: " | members[0] | ", " | members[1])
            quit()
        
        for sameItem in sameItems:
            if members[2].find(sameItem) != -1:
                break
        else:
            print("Cannot find an equal item between " | sameItems | "' on third member: " | members[2])
            quit()

        priority += calcPriority(sameItem)

if __name__ == "__main__":
    main()