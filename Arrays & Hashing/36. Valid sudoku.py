board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]


def sudoku_checker(board):
    n = 9 # sudoku board has 9 rows and 9 columns
    # create dictionaries for rows, columns and boxes, where already seen numbers would be stored. Allows to go through
    # the whole board only once => O(n) time complexity, but also O(n) space complexity
    seen_numbers_in_rows = {i: [] for i in range(n)}
    seen_numbers_in_columns = {i: [] for i in range(n)}
    seen_numbers_in_boxes = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                continue
            box = (i // 3) * 3 + (j // 3)  # formula to determine box number
            if board[i][j] not in seen_numbers_in_rows[i]:
                seen_numbers_in_rows[i].append(board[i][j])
            else:
                return False
            if board[i][j] not in seen_numbers_in_columns[j]:
                seen_numbers_in_columns[j].append(board[i][j])
            else:
                return False
            if board[i][j] not in seen_numbers_in_boxes[box]:
                seen_numbers_in_boxes[box].append(board[i][j])
            else:
                return False
    return True

print(sudoku_checker(board))
