import sys
from collections import deque

input = sys.stdin.readline

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def BFS(N, M):
    visit = [[0]*N for _ in range(N)]
    Q = deque()
    cnt = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] > M and visit[i][j]==0:
                Q.append([i,j])
                visit[i][j] = 1
                cnt += 1
                while Q:
                    r, c = Q.popleft()
                    visit[r][c] = 1
                    for k in range(4):
                        nr = r+dr[k]
                        nc = c+dc[k]
                        if nr<0 or nc<0 or nr>N-1 or nc>N-1 or area[nr][nc] <= M:
                            continue
                        if visit[nr][nc]==1 or [nr,nc] in Q:
                            continue
                        Q.append([nr,nc])
    return cnt


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
safe_area = 0

for M in range(0,101):
    safe_area = max(BFS(N, M),safe_area)
print(safe_area)
