import numpy as np

class Position:
    def __init__ (self, row = 0,col = 0):
        self.row = row
        self.col = col
    
    def move(self, offset):
        self.row += offset.row
        self.col += offset.col

class Space:
    def __init__ (self):
        self.m = np.asmatrix([0])

    def surface(self):
        return np.sum(self.m)

    def set(self, position, value):
        self.m[position.row, position.col] = value

    def extend(self, direction, size = 1):
        rows, cols = self.m.shape

        match direction:
            case 'U':
                newrow = np.zeros((size, cols), int)
                self.m = np.vstack((newrow, self.m))
            case 'D':
                newrow = np.zeros((size, cols), int)
                self.m = np.vstack((self.m, newrow))
            case 'L':
                newcol = np.zeros((rows, size), int)
                self.m = np.hstack((newcol, self.m))
            case 'R':
                newcol = np.zeros((rows, size), int)
                self.m = np.hstack((self.m, newcol))

    def extend_by_position(self, position):
        rows, cols = self.m.shape
        offset = Position(0,0)

        if(position.row > rows - 1):
            self.extend('D')

        if(position.col > cols - 1):
            self.extend('R')
        
        if(position.col < 0):
            self.extend('L')
            offset = Position(0,1)
        
        if(position.row < 0):
            self.extend('U')
            offset = Position(1,0)
        
        return offset

class Rope:
    def __init__(self, knots=1, space = Space()):
        self.space = space
        self.head = Position()
        self.knots = []
        for knot in range(0, knots):
            self.knots.append(Position())

    def move(self, direction, steps):
        coordinates = { 'U': [-1,0], 'D': [1,0], 'L': [0,-1], 'R': [0,1] }
        offset_move = Position(coordinates[direction][0], coordinates[direction][1])

        # Split movement in single steps
        for step in range(0, steps):
            self.move_head(offset_move)
            prev_knot = self.head
            for knot in self.knots:
                self.move_knot(knot, prev_knot)
                prev_knot = knot
            self.space.set(Position(knot.row, knot.col), 1) # Flag space occupied by last knot

    def move_head(self, offset_move):
        self.head.move(offset_move)
        offset = self.space.extend_by_position(self.head)
        self.head.move(offset)
        for knot in self.knots:
            knot.move(offset)

    def move_knot(self, knot, prev_knot):
        # No knot movement, overlaps head
        if knot.row == prev_knot.row and knot.col == prev_knot.col:
            return Position()
        
        # Horizontal movement on the same row, check distance
        if prev_knot.row == knot.row:
            # Still touching?
            if abs(knot.col - prev_knot.col) == 1: # Yes, no knot movement
                return Position()
            # No, keep up!
            else:
                row_move = 0
                if prev_knot.col > knot.col:
                    col_move = 1 # Move right
                else:
                    col_move = -1 # Move left
        
        # Vertical movement on the same column, check distance
        else:
            if prev_knot.col == knot.col:
                # Still touching?
                if abs(knot.row - prev_knot.row) == 1: # Yes, no knot movement
                    return Position()
                # No, keep up!
                else:
                    col_move = 0
                    if prev_knot.row > knot.row:
                        row_move = 1 # Move down
                    else:
                        row_move = -1 # Move up
            # Diagonal movement
            else:
                # Still touching?
                if abs(knot.row - prev_knot.row) == 1 and abs(knot.col - prev_knot.col) == 1: # Yes, no knot movement
                    return Position()
                # No, keep up!
                if prev_knot.row > knot.row:
                    row_move = 1 # Move down
                else:
                    row_move = -1 # Move up

                if prev_knot.col > knot.col:
                    col_move = 1 # Move right
                else:
                    col_move = -1 # Move left

        knot.move(Position(row_move, col_move))
        self.space.extend_by_position(knot)

def quiz(input, knots):
    rope = Rope(knots)
    with open(input) as file:
        for line in file:
            line = line.replace("\n", "")
            (direction, steps) = line.split()
            rope.move(direction, int(steps))
    print("Surface covered for rope with "+str(knots)+" knot(s): ", rope.space.surface())
    return rope

def main():
    # rope = quiz("day9/input-test.txt", 1)
    rope = quiz("day9/input.txt", 9)
    print(rope.space.m)
if __name__ == "__main__":
    main()
