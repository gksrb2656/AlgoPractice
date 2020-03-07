from collections import deque
#[0,1,2,3] 하,우,상,좌

def BFS():
    global cnt
    while Q:
        k, r, c = Q.popleft()
        if k == L:
            return
        if not visit[r][c]:
            cnt += 1
            visit[r][c] = 1
        if arr[r][c] == 1:
            Run(k,(0,1,2,3),r,c)
        elif arr[r][c] == 2:
            Run(k,(0,2),r,c)
        elif arr[r][c] == 3:
            Run(k,(1,3),r,c)
        elif arr[r][c] == 4:
            Run(k,(1,2),r,c)
        elif arr[r][c] == 5:
            Run(k,(0,1),r,c)
        elif arr[r][c] == 6:
            Run(k,(0,3),r,c)
        elif arr[r][c] == 7:
            Run(k,(2,3),r,c)

def Run(k,dir,r,c):
    for i in dir:
        if i == 0:
            nr = r+1
            if arr[nr][c] == 1 or arr[nr][c] == 2 or arr[nr][c] == 4 or arr[nr][c] == 7:
                if not visit[nr][c]:
                    Q.append((k+1,nr,c))

        if i == 1:
            nc = c+1
            if arr[r][nc] == 1 or arr[r][nc] == 3 or arr[r][nc] == 6 or arr[r][nc] == 7:
                if not visit[r][nc]:
                    Q.append((k+1,r,nc))
        if i == 2:
            nr = r-1
            if arr[nr][c] == 1 or arr[nr][c] == 2 or arr[nr][c] == 5 or arr[nr][c] == 6:
                if not visit[nr][c]:
                    Q.append((k+1,nr,c))
        if i == 3:
            nc = c - 1
            if arr[r][nc] == 1 or arr[r][nc] == 3 or arr[r][nc] == 4 or arr[r][nc] == 5:
                if not visit[r][nc]:
                    Q.append((k+1,r,nc))


T = int(input())
for t in range(1,T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [[0]*(M+2)]
    for i in range(N):
        arr.append([0]+list(map(int, input().split()))+[0])
    arr.append([0]*(M+2))
    visit = [[0]*(M+2) for _ in range(N+2)]
    Q = deque()
    cnt = 0
    Q.append((0,R+1,C+1))
    BFS()
    print("#{} {}".format(t,cnt))