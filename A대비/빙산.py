from collections import deque
import sys
sys.setrecursionlimit(10**6)
dr = (1,-1,0,0)
dc = (0,0,1,-1)
input = sys.stdin.readline

def BFS(r,c,year):
    Q.append((r,c))
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            for i in range(4):
                if nr>N-1 or nc>M-1 or nr<0 or nc<0:
                    continue
                if ice[nr][nc] and visit[nr][nc] != year:
                    Q.append((nr,nc))
                    visit[nr][nc] = year

def Melting(year):
    global total
    global time
    cnt = 0
    for r in range(N):
        for c in range(M):
            if ice[r][c]:
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if nr>N-1 or nc>M-1 or nr<0 or nc<0:
                        continue
                    if not ice[nr][nc]:
                        melt_b[r][c] += 1
                        total -= 1

    for r in range(N):
        for c in range(M):
            if ice[r][c]:
                ice[r][c] -= melt_b[r][c]
                melt_b[r][c] = 0
                if ice[r][c] < 0:
                    total += abs(ice[r][c])
                    ice[r][c] = 0

    for r in range(N):
        for c in range(M):
            if ice[r][c] and visit[r][c] != year:
                cnt += 1
                BFS(r,c,year)
                if cnt >= 2:
                    time = year
                    return
    if total == 0:
        return
    Melting(year+1)


N, M = map(int,input().split())
ice = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
melt_b = [[0] * M for _ in range(N)]
total = 0
for i in range(N):
    for j in range(M):
        if ice[i][j]:
            total += ice[i][j]
Q = deque()
time = 0
Melting(1)
print(time)