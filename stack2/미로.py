from collections import deque
from copy import deepcopy
# dr = [1,-1,0,0]
# dc = [0,0,1,-1]

# def BFS(v,G,visit):
#     global ans
#     visit.append(v)
#     if len(visit) > ans:
#         return
#     Q.append(v)
#     while Q:
#         r, c = Q.popleft()
#         for i in range(4):
#             nr = r+dr[i]
#             nc = c+dc[i]
#             if nr < 0 or nc < 0 or nr > N-1 or nc > M-1:
#                 continue
#             if [nr,nc] not in visit and G[nr][nc] == 1:
#                 BFS([nr,nc],G,deepcopy(visit))
#                 if [nr,nc] == [N-1,M-1]:
#                     if len(visit) < ans:
#                         ans = len(visit)+1
#                     return

# def BFS(v,G):
#     global ans
#     visit.append(v)
#     Q.append((v,1))
#     while Q:
#         rc,l = Q.popleft()
#         r = rc[0]
#         c = rc[1]
#         for i in range(4):
#             if ans < l:
#                 break
#             nr = r+dr[i]
#             nc = c+dc[i]
#             if nr < 0 or nc < 0 or nr > N-1 or nc > M-1:
#                 continue
#             if [nr, nc] == [N - 1, M - 1]:
#                 if ans > l:
#                     ans = l
#                 else:
#                     break
#                 return
#             if [nr,nc] not in visit and G[nr][nc] == 1:
#                 Q.append(([nr,nc],l + 1))
#                 visit.append([nr,nc])
#             else:
#                 visit.append([nr,nc])


from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]


N, M = map(int, input().split())
maze = [list(map(int,list(input()))) for _ in range(N)]
Q = deque()
Q.append(([0,0],1))
ans = N*M

visit = []

while Q:
    rc, l = Q.popleft()
    r = rc[0]
    c = rc[1]
    visit.append([r, c])
    for i in range(4):
        if ans < l + 1:
            break
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nc < 0 or nr > N - 1 or nc > M - 1:
            continue
        if [nr, nc] == [N - 1, M - 1]:
            if ans > l+1:
                ans = l+1
        if [nr, nc] not in visit and maze[nr][nc] == 1:
            Q.append(([nr, nc], l + 1))
print(ans)

# N, M = map(int, input().split())
# maze = [list(map(int,list(input()))) for _ in range(N)]
# graph = []
# Q = deque()
# Q.append(([0,0],1))
# ans = N*M
#
# for i in range(N):
#     for j in range(M):
#         if maze[i][j] == 1:
#             graph.append([i][j])

