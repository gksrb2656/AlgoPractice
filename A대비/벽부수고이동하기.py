from collections import deque
dr = [1,0,-1,0]
dc = [0,1,0,-1]

def BFS():
    Q.append((0,0,1,0))
    while Q:
        r,c,k,flag = Q.popleft()
        for d in range(4):
            nr,nc = r+dr[d], c+dc[d]
            if nr>N-1 or nc>M-1 or nr<0 or nc<0 or visit[nr][nc]==1:continue
            if flag and visit[nr][nc]:continue
            if arr[nr][nc]:
                if not flag:
                    visit[nr][nc] = 1
                    Q.append((nr,nc,k+1,1))
                    continue
                else:continue
            if (nr,nc) == (N-1,M-1):
                return k+1
            visit[nr][nc] = flag+1
            Q.append((nr,nc,k+1,flag))
    return -1

N, M = map(int, input().split())
arr = [list(map(int,(list(input())))) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
visit[0][0] = 1
MAX = -1
Q = deque()
if (N,M) == (1,1):print(1)
else: print(BFS())