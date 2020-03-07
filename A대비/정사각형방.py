from collections import deque
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def BFS(k, i, j):
    global r_n
    global point
    Q = deque()
    cnt = 1
    Q.append((i, j))
    visit[i][j] = k
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nc < 0 or nr > N - 1 or nc > N - 1: continue
            if arr[r][c] + 1 == arr[nr][nc]:
                Q.append((nr, nc))
                visit[nr][nc] = k
                cnt += 1
    if cnt > r_n or (cnt == r_n and k < point):
        r_n = cnt
        point = k

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    r_n = 0
    point = 0
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
            	BFS(arr[i][j], i, j)

    print("#{} {} {}".format(t, point, r_n))