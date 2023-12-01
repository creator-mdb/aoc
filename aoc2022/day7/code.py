from bigtree import Node, print_tree, findall

def cd(currentDir, param):
    if param == "..":
        return currentDir.parent if currentDir != None else None
    else:
        children = currentDir.children if currentDir != None else []
 
 #       for child in children:
 #           if child.node_name == param:
 #               return child
 #       return Node(param, type="dir", size= 0, parent = currentDir)
    return next((child for child in children if child.node_name == param), Node(param, type="dir", size= 0, parent = currentDir))

def parseLs(currentDir, line):
    (size, name) = line.split()

    # Ignore directories
    if size == "dir":
        return
    
    size = int(size)

    Node(name, type="file", size=size, parent = currentDir)

def updateDir(dir):
    if dir == None:
        return
    
    files = dir.children
    totalSize = 0

    for file in files:
        totalSize += file.size
    
    dir.size = totalSize

    updateDir(dir.parent)

def buildTree():
    currentDir = None
    expectLsOutput = False

    with open("day7/input.txt") as file:
        for line in file:  
            line = line.replace("\n", "")
            if line[0] == "$":
                # Is a command
                expectLsOutput = False
                cmd = line[2:].split()
                if cmd[0] == "cd":
                    currentDir = cd(currentDir, cmd[1])
                    continue
                if cmd[0] == "ls":
                    expectLsOutput = True
                    # Skip it
                    continue
                else:
                    print("Unknown command: " + line)
            else:
                # Is command output
                if expectLsOutput == True:
                    parseLs(currentDir, line)
                    updateDir(currentDir)
                else:
                    print("Garbage data: " + line)
    return currentDir.root

def find100kDirsTotalSize(dir):
    dirs = findall(dir, lambda node: node.size < 100000 and node.type == "dir")
    totalSize = 0
    for dir in dirs:
        totalSize += dir.size

    return totalSize

def findRightDirToDelete(dir, storageSpace, freeSpaceRequired):
    usedSpace = storageSpace - dir.size
    neededSpace = freeSpaceRequired - usedSpace
    dirs = findall(dir, lambda node: node.size >= neededSpace and node.type == "dir")
    #sizesList = []
    #for dir in dirs:
    #    sizesList.append(dir.size)
    #sizesList.sort()
    sizesList = sorted([dir.size for dir in dirs])
    return sizesList[0] 

def main():
    tree = buildTree()
    print_tree(tree, attr_list=["size", "type"])
    totalSize = find100kDirsTotalSize(tree)
    print("Total sum of dirs < 100K: " + str(totalSize))
    rightDirToDelete = findRightDirToDelete(tree, 70000000, 30000000)
    print("Right size to delete: " + str(rightDirToDelete))

if __name__ == "__main__":
    main()
