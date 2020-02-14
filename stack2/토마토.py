from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def BFS(G,st):
    visit=[]
    for i in st:
        Q.append((i,1))
        visit.append(i)
    while Q:
        rc,l = Q.popleft()
        for k in range(4):
            nr = rc[0] + dr[k]
            nc = rc[1] + dc[k]
            if nr < 0 or nc < 0 or nr > M - 1 or nc > N - 1:
                continue
            if G[nr][nc] == 0 and [nr,nc] not in visit:
                G[nr][nc] = l+1
                Q.append(([nr,nc],l+1))
            elif G[nr][nc] >l+1 and [nr,nc] not in visit:
                G[nr][nc] = l + 1
                Q.append(([nr, nc], l + 1))

def find(G):
    ans = 0
    for i in range(M):
        for j in range(N):
            if G[i][j] == 0:
                return -1
            elif G[i][j] > ans:
                ans = G[i][j]
    return ans-1

def st_p(G):
    st = []
    for i in range(M):
        for j in range(N):
            if G[i][j] == 1:
                st.append([i,j])

# def BFS(G):
#     for i in range(M):
#         visit = []
#         for j in range(N):
#             if tomato[i][j] == 1:
#                 Q.append([i,j])
#                 # visit.append([i,j])
#                 while Q:
#                     r,c = Q.popleft()
#                     visit.append([r,c])
#                     if r+1<=M-1 and [r+1,c] not in visit and tomato[r+1][c] == 0:
#                         Q.append([r+1,c])
#                         tomato[r+1][c] = tomato[r][c]+1
#                     elif r+1<=M-1 and [r+1,c] not in visit and tomato[r+1][c] > tomato[r][c]+1:
#                         Q.append([r + 1, c])
#                         tomato[r + 1][c] = tomato[r][c] + 1
#
#                     if r-1>=0 and [r-1,c] not in visit and tomato[r-1][c] == 0:
#                         Q.append([r-1,c])
#                         tomato[r-1][c] = tomato[r][c]+1
#                     elif r - 1 >= 0 and [r - 1, c] not in visit and tomato[r - 1][c] > tomato[r][c]+1:
#                         Q.append([r - 1, c])
#                         tomato[r - 1][c] = tomato[r][c] + 1
#
#                     if c+1<=N-1 and [r,c+1] not in visit and tomato[r][c+1] == 0:
#                         Q.append([r,c+1])
#                         tomato[r][c+1] = tomato[r][c]+1
#                     elif c+1 <= N-1 and [r, c+1] not in visit and tomato[r][c+1] > tomato[r][c]+1:
#                         Q.append([r, c + 1])
#                         tomato[r][c+1] = tomato[r][c] + 1
#
#                     if c-1>=0 and [r,c-1] not in visit and tomato[r][c-1] == 0:
#                         Q.append([r,c-1])
#                         tomato[r][c-1] = tomato[r][c]+1
#                     elif c-1>=0 and [r, c-1] not in visit and tomato[r][c-1] > tomato[r][c]+1:
#                         Q.append([r, c - 1])
#                         tomato[r][c-1] = tomato[r][c] + 1




N, M = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(M)]
Q = deque()
# visit = []
BFS(tomato)
print(find(tomato))


