dr = [1,0,-1,0]
dc = [0,1,0,-1]

def game(r,c,score,dir):
    global MAX
    nr,nc = r,c
    while 1:
        nr = nr+dr[dir]
        nc = nc+dc[dir]
        if (nr,nc) == (r,c):
            if score>MAX:
                MAX = score
            return
        if dir == 0 and nr > N-1:
            dir = (dir+2)%4
            score += 1
        elif dir == 1 and nc > N - 1:
            dir = (dir + 2) % 4
            score += 1
        elif dir == 2 and nr < 0:
            dir = (dir + 2) % 4
            score += 1
        elif dir == 3 and nc < 0:
            dir = (dir + 2) % 4
            score += 1
        elif board[nr][nc] == -1:
            if score>MAX:
                MAX = score
            return
        elif board[nr][nc] == 1:
            if dir == 0:# 1번 블록
                dir = 1
                score +=1
            elif dir == 3:
                dir = 2
                score +=1
            else:
                dir = (dir+2)%4
                score += 1
        elif board[nr][nc] == 2:# 2번 블록
            if dir == 2:  # 1번 블록
                dir = 1
                score += 1
            elif dir == 3:
                dir = 0
                score += 1
            else:
                dir = (dir + 2) % 4
                score += 1
        elif board[nr][nc] == 3:# 3번 블록
            if dir == 2:
                dir = 3
                score += 1
            elif dir == 1:
                dir = 0
                score += 1
            else:
                dir = (dir + 2) % 4
                score += 1
        elif board[nr][nc] == 4:# 4번 블록
            if dir == 0:
                dir = 3
                score += 1
            elif dir == 1:
                dir = 2
                score += 1
            else:
                dir = (dir + 2) % 4
                score += 1
        elif board[nr][nc] == 5:# 5번 블록
            dir = (dir + 2) % 4
            score += 1
        elif board[nr][nc] != 0:
            nr, nc = worm_hall(nr,nc)

def worm_hall(r, c):
    k = board[r][c]
    if (r,c) != worm[(k-6)*2]:
        return worm[(k-6)*2]
    else:
        return worm[(k - 6) * 2 + 1]

T = int(input())
for t in range(1,T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    MAX = 0
    worm = []
    for k in range(6,11):
        for i in range(N):
            for j in range(N):
                if board[i][j] == k:
                    worm.append((i,j))
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for k in range(4):
                    game(i,j,0,k)
    print("#{} {}".format(t, MAX))


