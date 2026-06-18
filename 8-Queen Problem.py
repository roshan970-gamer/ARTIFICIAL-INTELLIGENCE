N = 8
board = [[0]*N for _ in range(N)]

for i in range(N):
    board[i][i] = 1

for row in board:
    print(row)
