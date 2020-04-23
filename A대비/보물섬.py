from collections import deque
dr = [1,0,-1,0]
dc = [0,1,0,-1]

def BFS(i,j):
    global MAX
    visit = [data[:] for data in visit_original]
    visit[i][j] = 1
    while Q:
        r, c, k = Q.popleft()
        if k>MAX:
            MAX = k
        for d in range(4):
            nr = r+dr[d]
            nc = c+dc[d]
            if nr>N-1 or nc>M-1 or nr<0 or nc<0 or visit[nr][nc]:continue
            if MAP[nr][nc] == 'L':
                visit[nr][nc] = 1
                Q.append((nr,nc,k+1))

N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
visit_original = [[0]*M for _ in range(N)]
Q = deque()
MAX = 0
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 'L':
            Q.append((i,j,0))
            BFS(i,j)

print(MAX)