from collections import deque
import sys
from copy import deepcopy

dr = [1,-1,0,0]
dc = [0,0,1,-1]

input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
space = []
virus = []
K=0
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            space.append([i,j])
            K += 1
        elif lab[i][j] == 2:
            virus.append([i,j])


comb = []
MIN = N*M
# for i in range(K):
#     for j in range(i+1,K):
#         for k in range(j+1,K):
#             comb.append([space[i],space[j],space[k]])
# for i in comb:
#     Q = deque()
#     visit = []
#     cnt = 0
#     for j in i:
#         lab[j[0]][j[1]] = 1
#     for k in virus:
#         Q.append(k)
#     while Q:
#         r,c = Q.popleft()
#         cnt += 1
#         if cnt > MIN:
#             break
#         for l in range(4):
#             nr = r + dr[l]
#             nc = c + dc[l]
#             if nr<0 or nc<0 or nr>N-1 or nc>M-1 or [nr,nc] in visit:
#                 continue
#             if lab[nr][nc] != 0:
#                 continue
#             Q.append([nr,nc])
#             visit.append([nr, nc])
#     MIN = min(cnt, MIN)
#     for m in i:
#         lab[m[0]][m[1]] = 0

for i in range(K):
    for j in range(i+1,K):
        for k in range(j+1,K):
            copy_lab = deepcopy(lab)
            copy_lab[space[i][0]][space[i][1]] = 1
            copy_lab[space[j][0]][space[j][1]] = 1
            copy_lab[space[k][0]][space[k][1]] = 1
            Q = deque()
            cnt = 0
            for l in virus:
                Q.append(l)
            while Q:
                r,c = Q.popleft()
                cnt += 1
                if cnt > MIN:
                    break
                for m in range(4):
                    nr = r + dr[m]
                    nc = c + dc[m]
                    if nr<0 or nc<0 or nr>N-1 or nc>M-1:
                        continue
                    if copy_lab[nr][nc] != 0:
                        continue
                    Q.append([nr,nc])
                    copy_lab[nr][nc] = 2
            MIN = min(cnt, MIN)
            copy_lab[space[i][0]][space[i][1]] = 0
            copy_lab[space[j][0]][space[j][1]] = 0
            copy_lab[space[k][0]][space[k][1]] = 0

print(K - MIN - 3 + len(virus))