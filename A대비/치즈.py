# from collections import deque
# import sys
# sys.setrecursionlimit(10**6)
#
# dr = [0,1,0,-1]
# dc = [1,0,-1,0]
#
# def Melting(k,total):
#     global time
#     visit_b = [[0] * M for _ in range(N)]
#
#     BFS(k,visit_b)
#     for i in range(N):
#         for j in range(M):
#             if melt_b[i][j]==k:
#                 cheese[i][j] = 0
#                 total -= 1
#     if total != 0:
#         Melting(k+1,total)
#         cheese_num.append(total)
#     else:
#         time = k
#         return
#
#
# def BFS(k,visit_b):
#     Q.append((0,0))
#     while Q:
#         r, c = Q.popleft()
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if nr>N-1 or nc>M-1 or nr<0 or nc<0:
#                 continue
#             if cheese[nr][nc]:
#                 melt_b[nr][nc] = k
#             elif not visit_b[nr][nc]:
#                 Q.append((nr,nc))
#                 visit_b[nr][nc] = 1
#
# N, M = map(int, input().split())
# cheese = [list(map(int, input().split())) for _ in range(N)]
# melt_b = [[0]*M for _ in range(N)]
# Q = deque()
# total = 0
# time = 0
# cheese_num = []
# for i in range(N):
#     for j in range(M):
#         if cheese[i][j]:
#             total += 1
# Melting(1,total)
# print(time)
# if cheese_num:
#     print(cheese_num[0])
# else:
#     print(total)

##DFS##
import sys
sys.setrecursionlimit(1000000)

dr = [1,0,-1,0]
dc = [0,1,0,-1]
def DFS(r,c):
    for d in range(4):
        nr = r+dr[d]
        nc = c+dc[d]
        if nr>N-1 or nc>M-1 or nr<0 or nc<0 or arr[nr][nc] or visit[nr][nc]:continue
        visit[nr][nc] = 1
        DFS(nr,nc)

def melt(r, c):
    global total, cnt, flag
    if not total:
        return
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if nr > N - 1 or nc > M - 1 or nr < 0 or nc < 0: continue
        if visit[nr][nc] == 1:
            visit[nr][nc] = 0
            melt(nr, nc)
        elif arr[nr][nc]:
            total -= 1
            arr[nr][nc] = 0
            if total == 0:
                flag = True
                return

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
total = 0
cnt = 0
remain = []
visit = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            total += 1

flag = False
last = total
while not flag:
    cnt += 1
    DFS(0, 0)
    melt(0, 0)
    if total:
        last = total
print(cnt)
print(last)