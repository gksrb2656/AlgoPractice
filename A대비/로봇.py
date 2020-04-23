# from collections import deque
#
# dr = [-1,0,1,0]
# dc = [0,1,0,-1]
# D = {1:1, 2:3, 3:2, 4:0}
#
# def BFS():
#     while Q:
#         r, c, d, n, g = Q.popleft()
#         cnt = 0
#         if visit[er-1][ec-1]:
#             if n>= visit[er-1][ec-1]:
#                 continue
#         for _ in range(4):
#             nr = r+dr[d]
#             nc = c+dc[d]
#             if nr>M-1 or nc>N-1 or nr<0 or nc<0 or 0<visit[nr][nc] or arr[nr][nc]:
#                 d = (d+1)%4
#                 cnt += 1
#                 continue
#             if (nr,nc) == (er-1,ec-1):
#                 if d==D[ed]:
#                     if not cnt:
#                         g+=1
#                         visit[nr][nc] = min(visit[nr][nc],n+g//4)
#                     else:
#                         visit[nr][nc] = min(visit[nr][nc],n + cnt // 3 + cnt % 3 + 1)
#                 else:
#                     if not cnt:
#                         g += 1
#                         d_n = abs(D[ed] - d)
#                         visit[nr][nc] = min(visit[nr][nc],n + d_n // 3 + d_n % 3 + g//4)
#                     else:
#                         d_n = abs(D[ed] - d)
#                         visit[nr][nc] = min(visit[nr][nc],n + d_n // 3 + d_n % 3 + cnt//3+cnt%3 + 1)
#                 continue
#             if not cnt:
#                 if not g%3:
#                     Q.append((nr, nc, d, n+1, 1))
#                     visit[nr][nc] = n+1
#                 else:
#                     Q.append((nr,nc,d,n,g+1))
#                     visit[nr][nc]=n
#                 cnt += 1
#                 d = (d+1)%4
#             else:
#                 Q.append((nr,nc,d,n+cnt//3+cnt%3+1,1))
#                 visit[nr][nc]=n+cnt//3+cnt%3+1
#                 cnt += 1
#                 d = (d+1)%4
#
# M, N = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(M)]
# visit = [[0]*N for _ in range(M)]
# sr, sc, sd =map(int, input().split())
# er, ec, ed = map(int, input().split())
# Q = deque()
# Q.append((sr-1,sc-1,D[sd],0,0))
# visit[sr-1][sc-1] = 1
# visit[er-1][ec-1] = 10001
# BFS()
# print(visit[er-1][ec-1])
#
# for jj in visit:
#     print(jj)

from collections import deque

dr = [-1,0,1,0]
dc = [0,1,0,-1]
D = {1:1, 2:3, 3:2, 4:0}

def BFS():
    while Q:
        r, c, d, n= Q.popleft()
        if (r,c,d) == (er-1,ec-1,D[ed]):
            return n
        for k in range(-1,2,2):
            nd = (d+k)%4
            if visit[r][c][nd]: continue
            Q.append((r,c,nd,n+1))
            visit[r][c][nd] = n+1
        for i in range(1, 4):
            nr = r + dr[d] * i
            nc = c + dc[d] * i
            if nr > M - 1 or nc > N - 1 or nr < 0 or nc < 0 or visit[nr][nc][d]:continue
            if arr[nr][nc]:break
            Q.append((nr,nc,d,n+1))
            visit[nr][nc][d] = n+1

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visit = [[[0]*4 for _ in range(N)] for _ in range(M)]
sr, sc, sd =map(int, input().split())
er, ec, ed = map(int, input().split())
Q = deque()
Q.append((sr-1,sc-1,D[sd],0))
visit[sr-1][sc-1][D[sd]] = 1
print(BFS())
