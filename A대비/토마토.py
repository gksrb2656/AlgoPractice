import sys
from collections import deque
input = sys.stdin.readline
dr = [1,-1,0,0]
dc = [0, 0, 1, -1]


N, M = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(M)]
Q = deque()
e_p = 0
days = 1
for i in range(M):
    for j in range(N):
        if tomato[i][j] == 1:
            Q.append([i,j])
        elif tomato[i][j] == 0:
            e_p += 1
while Q:
    r, c = Q.popleft()
    for j in range(4):
        nr = r + dr[j]
        nc = c + dc[j]
        if nr<0 or nc<0 or nr>M-1 or nc>N-1:
            continue
        if tomato[nr][nc] != 0:
            continue
        tomato[nr][nc] = tomato[r][c] + 1
        Q.append([nr,nc])
        e_p -= 1
        days = max(days, tomato[nr][nc])
if e_p != 0:
    print(-1)
else:
    print(days-1)

# if e_p == 0:
#     print(0)
# else:
#     BFS(e_p,days)
    # MAX = 0
    # for i in range(M):
    #     for j in range(N):
    #         if tomato[i][j] == 0:
    #             MAX = 0
    #             break
    #         elif tomato[i][j] > MAX:
    #             MAX = tomato[i][j]
    #     if MAX == 0:
    #         break
    # print(MAX-1)
# for i in tomato:
#     print(i)