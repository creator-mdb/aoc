def areAllElementsDifferent(inputStr):
    inputSet = set(inputStr)
    if len(inputStr) == len(inputSet):
        return True
    else: 
        return False

def main():
    sparkSize = 14
    with open("day6/input.txt") as file:
        buffer = file.read().rstrip()

    for i in range(0, len(buffer) - sparkSize):
        chunkEndPos = i + sparkSize
        if areAllElementsDifferent(buffer[i:chunkEndPos]) == True:
            print(buffer[i:chunkEndPos] + ": first marker after character " + str(chunkEndPos))
            quit()
    print("marker not found")

if __name__ == "__main__":
    main()
