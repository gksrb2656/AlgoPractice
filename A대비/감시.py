# from copy import deepcopy
#
# def DFS(k,arr):
#     global ans
#     global total
#     if k== total:
#         cnt = 0
#         for i in range(1, N + 1):
#             cnt += arr[i].count(0)
#         ans = min(ans,cnt)
#         return
#
#     Type(k,arr)
#
#
# def observe(dir,r,c,arr):
#     arr_copy = deepcopy(arr)
#     nr, nc = r, c
#     for i in dir:
#         if i == 0:
#             while 1:
#                 nr += 1
#                 if arr[nr][c] == 6: break
#                 if arr[nr][c] != 0: continue
#                 arr_copy[nr][c] ="#"
#         elif i == 1:
#             while 1:
#                 nc += 1
#                 if arr[r][nc] == 6: break
#                 if arr[r][nc] != 0: continue
#                 arr_copy[r][nc] = "#"
#         elif i == 2:
#             while 1:
#                 nr -= 1
#                 if arr[nr][c] == 6: break
#                 if arr[nr][c] != 0: continue
#                 arr_copy[nr][c] = "#"
#         elif i == 3:
#             while 1:
#                 nc -= 1
#                 if arr[r][nc] == 6: break
#                 if arr[r][nc] != 0: continue
#                 arr_copy[r][nc] = "#"
#     return arr_copy
#
# def Type(k,arr):
#     r, c, type = observers[k]
#     if type == 1:
#         for i in range(4):
#             nxt_arr = observe([i],r,c,arr)
#             DFS(k+1,nxt_arr)
#     elif type == 2:
#         for i in [(0,2),(1,3)]:
#             nxt_arr =observe(i,r,c,arr)
#             DFS(k+1,nxt_arr)
#     elif type == 3:
#         for i in [(0, 1), (1, 2), (2, 3), (3, 0)]:
#             nxt_arr =observe(i,r,c,arr)
#             DFS(k+1,nxt_arr)
#     elif type == 4:
#         for i in [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)]:
#             nxt_arr =observe(i, r, c, arr)
#             DFS(k + 1,nxt_arr)
#     elif type == 5:
#         nxt_arr = observe((0,1,2,3),r,c,arr)
#         DFS(k+1,nxt_arr)
#
#
# N, M = map(int, input().split())
# arr = [[6]*(M+2)]
# for _ in range(N):
#     arr.append([6]+list(map(int, input().split()))+[6])
# arr.append([6]*(M+2))
# total = 0
# observers = []
# ans = N*M
# for i in range(1,N+1):
#     for j in range(1,M+1):
#         if 1<=arr[i][j]<=5:
#             total += 1
#             observers.append((i,j,arr[i][j]))
#
# DFS(0,arr)
# print(ans)

MIS = lambda: map(int,input().split())
from itertools import product

def union(sets):
    res = set()
    for s in sets: res|= s
    return res

def sight(i0, j0):
    for di, dj in (1,0), (-1,0), (0,1), (0,-1):
        i, j = i0, j0
        seen = set()
        while 0<=i<n and 0<=j<m and grid[i][j] != 6:
            seen.add((i,j))
            i+= di; j+= dj
        yield seen

n, m = MIS()
grid = [list(MIS()) for i in range(n)]
camera = []
empty = 0
for i in range(n):
    for j in range(m):
        c = grid[i][j]
        if c == 6: continue
        empty+= 1
        if c == 0: continue
        D, U, R, L = sight(i, j)
        if c == 1: camera.append([D,U,R,L])
        elif c == 2: camera.append([D|U, R|L])
        elif c == 3: camera.append([U|R, U|L, D|R, D|L])
        elif c == 4: camera.append([D|U|R, D|U|L, R|L|U, R|L|D])
        else: camera.append([D|U|R|L])
print(min(empty - len(union(P)) for P in product(*camera)))