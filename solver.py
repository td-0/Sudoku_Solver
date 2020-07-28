# A Sudoku Solving Program

import sys
from computation import solve

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("ERROR: Invalid Number of Arguments")
        sys.exit()

    input_file = open(sys.argv[1], "r")
    has_output = False
    if len(sys.argv) > 2:
        output_file = open(sys.argv[2], "w")
        has_output = True


    board = {}

    y_offset = 0
    for y in range(13):
        if y == 0 or y % 4 == 0:
            input_file.readline()
            y_offset += 1
            continue
        curr_line = input_file.readline()
        x_offset = 0
        for x in range(len(curr_line) - 1):
            if curr_line[x] == '|':
                x_offset += 1
                continue
            board[(x - x_offset, y - y_offset)] = curr_line[x]

    solved_board = solve(board)
    count = 0
    while solved_board == False:
        solved_board = solve(board)
        count += 1
        print(count)

    if has_output:
        print_board(solved_board, output_file)
    else:
        print_board(solved_board, None)



    input_file.close()
    if has_output:
        output_file.close()


def print_board(board, file):
    caps = "-------------"
    dividers = "|-----------|"

    if file == None:
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
                    line += board[(p - p_offset, l - l_offset)]
                print(line)

    if file != None:
        p_offset = 0
        for p in range(13):
            if p == 0 or p == 12:
                p_offset += 1
                file.write(caps + '\n')
            elif p % 4 == 0:
                p_offset += 1
                file.write(dividers + '\n')
            else:
                line = ""
                l_offset = 0
                for l in range(13):
                    if l == 0 or l % 4 == 0:
                        l_offset += 1
                        line += "|"
                        continue
                    line += board[(p - p_offset, l - l_offset)]
                file.write(line + '\n')


if __name__ == "__main__":
    main()
