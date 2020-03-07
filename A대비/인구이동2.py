from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]

def Move(k):
    n = 0
    flag = False
    visit = [[[0] * 2 for _ in range(N)] for _ in range(N)]
    for i1 in range(N):
        for j1 in range(N):
            if visit[i1][j1][0] != k+1:
                Q.append((i1,j1))
                sum_people = 0
                cnt = 0
                n += 1
                while Q:
                    r, c = Q.popleft()
                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if nr < 0 or nc < 0 or nr > N - 1 or nc > N - 1: continue
                        if L <= abs(arr[r][c] - arr[nr][nc]) <= R and visit[nr][nc][0] != n:
                            Q.append((nr, nc))
                            visit[nr][nc][0] = n
                            sum_people += arr[nr][nc]
                            cnt += 1

                if sum_people:
                    flag = True
                    for i in range(N):
                        for j in range(N):
                            if visit[i][j][0] == n:
                                visit[i][j][1] = sum_people // cnt
    if flag:
        for i in range(N):
            for j in range(N):
                if visit[i][j][0]:
                    arr[i][j] = visit[i][j][1]

        Move(k+1)
    else:
        return print(k)


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

Q = deque()
Move(0)
