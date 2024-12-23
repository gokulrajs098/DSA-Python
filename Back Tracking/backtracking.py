def is_Safe(board, row, col, N):
    i = col
    while i >=0:
        if board[row][i] == 1:
            return False
        i -= 1
    i = col
    j = row

    while i >= 0 and j >=0:
        if board[j][i] == 1:
            return False
        i -= 1
        j -= 1
    
    i = col
    j = row

    while i >= 0 and j <N:
        if board[j][i] == 1:
            return False
        i -=1
        j +=1
    return True

    
def solution(board, N, col):    

    if col >= N:
        return True
    
    for row in range(N):
        if is_Safe(board, row, col, N):
            board[row][col] = 1

            if solution(board, N, col + 1):
                return True
            board[row][col] = 0
    return False


# Print the board in a readable format
def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))

# Initialize and run the solution
N = 4
board = [[0 for i in range(N)] for i in range(N)]
print("Initial Board:")
print_board(board)

start = 0
result = solution(board, N, start)
if result:
    print("\nSolution:")
    print_board(board)
else:
    print(None)
