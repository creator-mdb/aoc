import numpy as np

def is_tree_visible(m, tree_row, tree_col):
    rows, columns = m.shape
    visible_sides = 4
    tree_height = m.item(tree_row, tree_col)

    # col-axis visibility check, left side
    current_range = range(0, tree_col)
    for col in current_range:
        if m.item(tree_row, col) >= tree_height:
            visible_sides -= 1
            break

    # col-axis visibility check, right side
    current_range = range((tree_col+1), columns)
    for col in current_range:
        if m.item(tree_row, col) >= tree_height:
            visible_sides -= 1
            break

    # row-axis visibility check, top side
    current_range = range(0, tree_row)
    for row in current_range:
        if m.item(row, tree_col) >= tree_height:
            visible_sides -= 1
            break

    # row-axis visibility check, bottom side
    current_range = range((tree_row+1), rows)
    for row in current_range:
        if m.item(row, tree_col) >= tree_height:
            visible_sides -= 1
            break

    return visible_sides > 0

def scenic_score(m, tree_row, tree_col):
    rows, columns = m.shape
    score = 0
    tree_height = m.item(tree_row, tree_col)

    # col-axis score, left side
    scenic_trees = 0
    current_range = reversed(range(0, tree_col))
    for col in current_range:
        if m.item(tree_row, col) < tree_height:
            scenic_trees += 1
        else:
            scenic_trees += 1
            break
    score = scenic_trees

    # col-axis score, right side
    scenic_trees = 0
    current_range = range((tree_col+1), columns)
    for col in current_range:
        if m.item(tree_row, col) < tree_height:
            scenic_trees += 1
        else:
            scenic_trees += 1
            break
    score = score * scenic_trees

    # row-axis score, top side
    scenic_trees = 0
    current_range = reversed(range(0, tree_row))
    for row in current_range:
        if m.item(row, tree_col) < tree_height:
            scenic_trees += 1
        else:
            scenic_trees += 1
            break
    score = score * scenic_trees

    # row-axis score, bottom side
    scenic_trees = 0
    current_range = range((tree_row+1), rows)
    for row in current_range:
        if m.item(row, tree_col) < tree_height:
            scenic_trees += 1
        else:
            scenic_trees += 1
            break

    return score * scenic_trees

def main():
    int_rows = []
    with open("day8/input.txt") as file:
        for line in file:  
            line = line.replace("\n", "")
            int_rows.append([int(x) for x in line])

    m = np.asmatrix(int_rows)
    rows, columns = m.shape

    visible_trees = (rows-1) * 2 + (columns-1) * 2
    for row in range(1, rows - 1):
        for col in range(1, columns - 1):
            if is_tree_visible(m, row, col) == True:
                visible_trees += 1 

    print("There are ",visible_trees," visible trees")

    top_scenic_score = 0
    for row in range(rows):
        for col in range(columns):
            current_scenic_score = scenic_score(m, row, col)
            if current_scenic_score > top_scenic_score:
                top_scenic_score = current_scenic_score

    print("Top scenic score is ",top_scenic_score)

if __name__ == "__main__":
    main()
