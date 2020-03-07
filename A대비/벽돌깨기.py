from collections import deque

dir = {0: (1, 0), 1: (-1, 0), 2: (0, 1), 3: (0, -1)}

def DFS(k, G,total):
    global ans
    if k == N or total == 0:
        if ans>total:
            ans = total
        return

    for i in range(W-1,-1,-1):
        for j in range(H):
            if G[i][j]:
                G_copy = [data[:] for data in G]
                Total = total- 1
                Q.append((i, j, G[i][j]-1))
                while Q:
                    G[i][j] = 0
                    r, c, ex = Q.popleft()
                    for n in range(1, ex + 1):
                        for d in range(4):
                            nr, nc = r + dir[d][0] * n, c + dir[d][1] * n
                            if nr > W - 1 or nc > H - 1 or nr < 0 or nc < 0 or not G[nr][nc]: continue
                            if G[nr][nc] > 1:
                                Q.append((nr, nc, G[nr][nc] - 1))
                            G[nr][nc] = 0
                            Total -= 1
                move(G)
                DFS(k+1,G, Total)
                G = G_copy
                break


# def explode(G,ex_range,i,j,total):
#     G[i][j] = 0
#     total -= 1
#     Q.append((i,j,ex_range))
#     while Q:
#         r,c,k = Q.popleft()
#         for n in range(1,k+1):
#             for d in range(4):
#                 nr, nc = r + dir[d][0] * n,c + dir[d][1] * n
#                 if nr>W-1 or nc>H-1 or nr<0 or nc<0 or not G[nr][nc]:continue
#                 if G[nr][nc]>1:
#                     Q.append((nr,nc,G[nr][nc]-1))
#                 G[nr][nc] = 0
#                 total -=1
#     return total


def move(G):
    for i in range(W):
        z_cnt = G[i].count(0)
        for _ in range(z_cnt):
            G[i].remove(0)
        G[i] = [0]*z_cnt+G[i]

T = int(input())
for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    arr_reverse = [[0] * H for _ in range(W)]
    total = 0
    Q = deque()
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                total += 1
            arr_reverse[j][i] = arr[i][j]

    ans = 400
    DFS(0,arr_reverse,total)
    print("#{} {}".format(t,ans))

###좋은 풀이###
# def sol(n, COUNT, DATA):
#     global MIN
#
#     if n == N or not COUNT:
#         MIN = min(MIN, COUNT)
#         return
#
#     for w in range(W):
#
#         q = []
#         # 처음 부술 블럭 찾기
#         for i in range(H):
#             if DATA[i][w]:
#                 data = [j[:] for j in DATA]
#                 count = COUNT - 1
#                 q = [(i, w, data[i][w])]
#                 data[i][w] = 0
#                 break
#         if not q:
#             continue
#
#         # 블록 부수기
#         while q:
#             y, x, length = q.pop()
#             for k in range(1, length):
#                 for dy, dx in (0, 1), (0, -1), (1, 0), (-1, 0):
#                     ny, nx = y + dy * k, x + dx * k
#                     if -1 < ny < H and -1 < nx < W and data[ny][nx]:
#                         if data[ny][nx] > 1:
#                             q.append((ny, nx, data[ny][nx]))
#                         data[ny][nx] = 0
#                         count -= 1
#
#         # 떨어지기
#         for x in range(W):
#             idx = H - 1
#             for y in range(H - 1, -1, -1):
#                 if data[y][x]:
#                     data[idx][x], data[y][x] = data[y][x], data[idx][x]
#                     idx -= 1
#
#         sol(n + 1, count, data)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, W, H = map(int, input().split())
#     origin = [list(map(int, input().split())) for _ in range(H)]
#     count = sum(1 for x in origin for a in x if a)
#     MIN = 9999
#     sol(0, count, origin)
#     print("#{} {}".format(tc, MIN))