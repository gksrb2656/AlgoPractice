def move(dir, board, n):
    global answer

    b_copy = [b[:] for b in board]
    for _ in range(dir):
        b_copy = rotate(b_copy)
    for i in range(N):
        b_copy[i] = [data for data in b_copy[i] if data]
        b_copy[i] += (N-len(b_copy[i]))*[0]
    for i in range(N):
        for j in range(N - 1):
            if b_copy[i][j] == b_copy[i][j+1]:
                b_copy[i][j] = 2*b_copy[i][j]
                b_copy[i][j+1] = 0
        b_copy[i] = [data for data in b_copy[i] if data]
        b_copy[i] += (N-len(b_copy[i]))*[0]

    if n == 5:
        for r in range(N):
            for c in range(N):
                answer = max(answer,board[r][c])
        return

    move(0, b_copy, n + 1)
    move(1, b_copy, n + 1)
    move(2, b_copy, n + 1)
    move(3, b_copy, n + 1)


def rotate(board):
    temp = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[j][N-i-1] = board[i][j]
    return temp



N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer= 0

for i in range(4):
    move(i,board,0)

print(answer)