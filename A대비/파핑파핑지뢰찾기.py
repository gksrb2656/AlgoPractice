from collections import deque

dr = (1, 0, -1, 0, 1, 1, -1, -1)
dc = (0, 1, 0, -1, 1, -1, 1, -1)


def BFS(i, j):
    global total, cnt

    Q.append((i, j))
    while Q:
        r, c = Q.popleft()
        flag = 1
        for d in range(8):
            nr, nc = r + dr[d], c + dc[d]
            if nr > N - 1 or nc > N - 1 or nr < 0 or nc < 0 or visit[nr][nc]: continue
            if arr[nr][nc] == '*':
                flag = 0
                break
        if flag:
            if (r, c) == (i, j):
                cnt += 1
            if not visit[r][c]:
                total -= 1
            visit[r][c] = 1
            for d in range(8):
                nr, nc = r + dr[d], c + dc[d]
                if nr > N - 1 or nc > N - 1 or nr < 0 or nc < 0 or visit[nr][nc]: continue
                visit[nr][nc] = 1
                total -= 1
                Q.append((nr, nc))


for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    Q = deque()
    total = 0
    cnt = 0
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.':
                total += 1
                if visit[i][j]: continue
                BFS(i, j)
    print("#{} {}".format(t, cnt + total))