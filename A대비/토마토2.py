# from collections import deque
#
# def BFS():
#     global total
#     while Q:
#         r, c, k = Q.popleft()
#         for i in range(1,H+1):
#             for d in range(6):
#                 nr = r+dr[d]
#                 nc = c+dc[d]
#                 if nr>N*i-1 or nc>M-1 or nr<0 or nc<0 or visit[nr][nc]:continue
#                 if not tomatos[nr][nc]:
#                     Q.append((nr,nc,k+1))
#                     visit[nr][nc] = 1
#                     total -= 1
#                     if not total:
#                         return k+1
#     return -1
#
# M, N, H = map(int, input().split())
#
# dr = [1,0,-1,0,N,-N]
# dc = [0,1,0,-1,0,0]
#
# tomatos = [list(map(int, input().split())) for _ in range(N*H)]
# visit = [[0]*M for _ in range(N*H)]
# Q =deque()
# total = 0
# for i in range(N*H):
#     for j in range(M):
#         if tomatos[i][j] == 1:
#             Q.append((i,j,0))
#         elif not tomatos[i][j]:
#             total += 1
# if not total:
#     print(0)
# else:
#     print(BFS())

from collections import deque
import sys
input = sys.stdin.readline

def BFS():
    global total
    while Q:
        z, r, c, k = Q.popleft()
        for d in range(6):
            nr = r+dr[d]
            nc = c+dc[d]
            nz = z+dz[d]
            if nr>N-1 or nc>M-1 or nz>H-1 or nr<0 or nc<0 or nz<0 or visit[nz][nr][nc]:continue
            if not tomatos[nz][nr][nc]:
                Q.append((nz,nr,nc,k+1))
                visit[nz][nr][nc] = 1
                total -= 1
                if not total:
                    return k+1
    return -1

M, N, H = map(int, input().split())

dr = [1,0,-1,0,0,0]
dc = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]
tomatos =[[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
visit = [[[0]*M for _ in range(N)] for _ in range(H)]
Q =deque()
total = 0
for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomatos[k][i][j] == 1:
                Q.append((k,i,j,0))
            elif not tomatos[k][i][j]:
                total += 1
if not total:
    print(0)
else:
    print(BFS())