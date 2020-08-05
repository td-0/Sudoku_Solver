# Solves the given sudoku puzzle through backtracking

def solve(board):
    choice = None
    for coord in board:
        if board[coord] == ' ':
            choice = coord
            break

    if choice == None:
        return True

    for x in range(1, 10):
        if conflicts(str(x), domain(board, choice)) == False:
            board[choice] = str(x)
            if solve(board):
                return True
            else:
                board[choice] = ' '

    return False


def domain(board, coords):
    # Builds domain of coordinate when called

    x, y = coords
    row = set([])
    column = set([])
    box = set([])

    # Add row
    for a in range(9):
        if board[(a, y)] != ' ':
            row.add(board[(a, y)])

    # Add column
    for b in range(9):
        if board[(x, b)] != ' ':
            column.add(board[(x, b)])

    # Add box
    x_range = None
    y_range = None
    if x < 3:
        x_range = (0, 1, 2)
    elif x >= 3 and x < 6:
        x_range = (3, 4, 5)
    else:
        x_range = (6, 7, 8)

    if y < 3:
        y_range = (0, 1, 2)
    elif y >= 3 and y < 6:
        y_range = (3, 4, 5)
    else:
        y_range = (6, 7, 8)

    for c in x_range:
        for d in y_range:
            if board[(c, d)] != ' ':
                box.add(board[(c, d)])


    dom = [row, column, box]

    return dom


def conflicts(value, domain):
    # Check if new value conflicts with any value in its domain

    for group in domain:
        if value in group:
            return True

    return False
