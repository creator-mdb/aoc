import numpy as np

class Position:
    def __init__ (self, row=0,col=0):
        self.row = row
        self.col = col
    
    def shift(self, offset):
        self.row += offset.row
        self.col += offset.col

def extend_space(m, direction, size=1):
    rows, cols = m.shape

    match direction:
        case 'U':
            newrow = np.zeros((size, cols), int)
            return np.vstack((newrow, m))
        case 'D':
            newrow = np.zeros((size, cols), int)
            return np.vstack((m, newrow))
        case 'L':
            newcol = np.zeros((rows, size), int)
            return np.hstack((newcol, m))
        case 'R':
            newcol = np.zeros((rows, size), int)
            return np.hstack((m, newcol))
    return m

def fix_out_of_bounds(m, position):
    rows, cols = m.shape
    offset = Position(0,0)

    if(position.row > rows-1):
        m = extend_space(m, 'D')

    if(position.col > cols-1):
        m = extend_space(m, 'R')
    
    if(position.col < 0):
        m = extend_space(m, 'L')
        offset = Position(0,1)
    
    if(position.row < 0):
        m = extend_space(m, 'U')
        offset = Position(1,0)
    
    return (m, offset)

def do_step_head(m, head, row_move, col_move):
    head.row += row_move
    head.col += col_move
    (m, offset) = fix_out_of_bounds(m, head)
    return (m, head, offset)

def do_step_tail(m, tail, head):
    
    # No tail movement, overlaps head
    if tail.row == head.row and tail.col == head.col:
        return (m, tail, Position(0,0))
    
    # Horizontal movement on the same row, check distance
    if head.row == tail.row:
        # Still touching?
        if abs(tail.col-head.col) == 1: # Yes, no tail movement
            return (m, tail, Position(0,0))
        # No, keep up!
        else:
            row_move = 0
            if head.col > tail.col:
                col_move = 1 # Move right
            else:
                col_move = -1 # Moveleft
    
    # Vertical movement on the same column, check distance
    else:
        if head.col == tail.col:
            # Still touching?
            if abs(tail.row-head.row) == 1: # Yes, no tail movement
                return (m, tail, Position(0,0))
            # No, keep up!
            else:
                col_move = 0
                if head.row > tail.row:
                    row_move = 1 # Move down
                else:
                    row_move = -1 # Move up
        # Diagonal movement
        else:
            # Still touching?
            if abs(tail.row-head.row) == 1 and abs(tail.col-head.col) == 1: # Yes, no tail movement
                return (m, tail, Position(0,0))
            # No, keep up!
            if head.row > tail.row:
                row_move = 1 # Move down
            else:
                row_move = -1 # Move up

            if head.col > tail.col:
                col_move = 1 # Move right
            else:
                col_move = -1 # Move left

    tail.row += row_move
    tail.col += col_move

    (m, offset) = fix_out_of_bounds(m, tail)
    return (m, tail, offset)

def do_step(m, head, tail, new_pos):
    (m, head, offset) = do_step_head(m, head, new_pos.row, new_pos.col)
    head.shift(offset)
    tail.shift(offset)
    (m, tail, offset) = do_step_tail(m, tail, head)

    m[tail.row,tail.col] = 1 # Flag space occupied by tail
    return (m, head, tail)

def move(m, head, tail, direction, steps):
    directions = { 'U': [-1,0], 'D': [1,0], 'L': [0,-1], 'R': [0,1] }
    offset = Position(directions[direction][0], directions[direction][1])

    # Split movement in single steps
    for step in range(0, steps):
        (m, head, tail) = do_step(m, head, tail, offset)

    return (m, head, tail)

def main():
    m = np.asmatrix([0]) # Start space
    
    head = Position(0,0)
    tail = Position(0,0)
    with open("day9/input.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            (direction, steps) = line.split()
            (m, head, tail) = move(m, head, tail, direction, int(steps))
    print("Surface covered ", np.sum(m))

if __name__ == "__main__":
    main()

