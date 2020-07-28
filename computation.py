# Solves the given sudoku puzzle

import copy
import random

def solve(board):
    unassigned = set([])
    for coord in board:
        if board[coord] == ' ':
            unassigned.add(coord)

    new_board = board
    while len(unassigned) != 0:
        choice = random.choice(tuple(unassigned))
        new_board = find_value(new_board, choice)
        if new_board == False:
            return False
        unassigned.discard(choice)

    return new_board


def find_value(board, coords):
    dom = domain(board, coords)
    for attempt in range(1, 10):
        if conflicts(str(attempt), dom) == False:
            break

    if attempt == 9:
        return False

    new_board = copy.deepcopy(board)
    new_board[coords] = str(attempt)

    return new_board


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
