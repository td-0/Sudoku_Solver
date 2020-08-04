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
        choice = fullest_domain(board, unassigned)
        #print_board(new_board)
        new_board = find_value(new_board, choice)
        if new_board == False:
            #print_board(board)
            return False
        unassigned.discard(choice)

    return new_board


# TEMPORARY
def print_board(board):
    caps = "-------------"
    dividers = "|-----------|"

    p_offset = 0
    for p in range(13):
        if p == 0 or p == 12:
            p_offset += 1
            print(caps)
        elif p % 4 == 0:
            p_offset += 1
            print(dividers)
        else:
            line = ""
            l_offset = 0
            for l in range(13):
                if l == 0 or l % 4 == 0:
                    l_offset += 1
                    line += "|"
                    continue
                line += board[(l - l_offset, p - p_offset)]
            print(line)


def find_value(board, coords):
    dom = domain(board, coords)
    possible = []
    for attempt in range(1, 10):
        if conflicts(str(attempt), dom) == False:
            possible.append(attempt)

    if len(possible) == 0:
        return False

    chosen = possible[random.randint(0, len(possible) - 1)]
    new_board = copy.deepcopy(board)
    new_board[coords] = str(chosen)

    return new_board


def fullest_domain(board, unassigned):
    # Returns unassigned coordinate with the most spaces in its domain filled
    # Largest Domain Size = Fullest Domain
    fullest = None
    largest_size = 0
    for coord in unassigned:
        dom = domain(board, coord)
        size = len(dom[0]) + len(dom[1]) + len(dom[2])
        if size > largest_size:
            largest_size = size
            fullest = coord

    return fullest


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
