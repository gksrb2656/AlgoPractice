# from collections import deque
# import sys
#
# dr = [1,-1,0,0]
# dc = [0,0,1,-1]
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# lab = [list(map(int, input().split())) for _ in range(N)]
# space = []
# virus = []
# K=0
# for i in range(N):
#     for j in range(M):
#         if lab[i][j] == 0:
#             space += [(i,j)]
#             K += 1
#         elif lab[i][j] == 2:
#             virus +=[(i,j)]
#
# MIN = N*M
# for i in range(K):
#     for j in range(i+1,K):
#         for k in range(j+1,K):
#             copy_lab = [data[:] for data in lab]
#             copy_lab[space[i][0]][space[i][1]] = 1
#             copy_lab[space[j][0]][space[j][1]] = 1
#             copy_lab[space[k][0]][space[k][1]] = 1
#             Q = deque()
#             cnt = 0
#             for l in virus:
#                 Q.append(l)
#             while Q:
#                 r,c = Q.popleft()
#                 cnt += 1
#                 if cnt >= MIN:
#                     break
#                 for m in range(4):
#                     nr = r + dr[m]
#                     nc = c + dc[m]
#                     if nr<0 or nc<0 or nr>N-1 or nc>M-1:
#                         continue
#                     if copy_lab[nr][nc] != 0:
#                         continue
#                     Q.append([nr,nc])
#                     copy_lab[nr][nc] = 2
#             MIN = min(cnt, MIN)
#             copy_lab[space[i][0]][space[i][1]] = 0
#             copy_lab[space[j][0]][space[j][1]] = 0
#             copy_lab[space[k][0]][space[k][1]] = 0
#
# print(K - MIN - 3 + len(virus))

from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def comb(n,K):
    if K <3 :
        for i in range(n,len(combs)):
            r = combs[i]//M
            c = combs[i]%M
            if not lab[r][c]:
                lab[r][c] = 1
                comb(i+1,K+1)
                lab[r][c] = 0
    else:
        copy_lab = [data[:] for data in lab]
        BFS(copy_lab)

def BFS(copy_lab):
    global MIN
    Q = deque()
    cnt = 0
    for v in viruses:
        Q.append(v)
    while Q:
        r,c = Q.popleft()
        cnt += 1
        if cnt >= MIN:
            return
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr<0 or nc<0 or nr>N-1 or nc>M-1 or copy_lab[nr][nc] != 0: continue
            Q.append((nr,nc))
            copy_lab[nr][nc] = 2
    MIN = min(MIN,cnt)

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
viruses = []
MIN = N*M
spaces = -3
combs = []
for i in range(N):
    spaces += lab[i].count(0)
    for j in range(M):
        if lab[i][j] == 2:
            viruses += [(i,j)]
        elif not lab[i][j]:
            combs += [i*M+j]

comb(0,0)
print(spaces-MIN+len(viruses))