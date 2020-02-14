dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def DFS(G,area = 0):
    for i in range(M):
        for j in range(N):
            if [i,j] in visit:
                continue
            visit.append([i,j])
            if G[i][j] == 1:
                area += 1
                stack.append([i,j])
                while stack:
                    r, c = stack.pop()
                    for d in range(4):
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if nr < 0 or nc < 0 or nr >M-1 or nc>N-1:
                            continue
                        if G[nr][nc] == 1 and [nr,nc] not in visit:
                            stack.append([nr,nc])
                            visit.append([nr, nc])
                        else:
                            visit.append([nr, nc])
    return area


T = int(input())
for t in range(1,T+1):
    visit= []
    stack = []
    area = 0
    M, N, K = map(int, input().split())
    point = [list(map(int,input().split())) for _ in range(K)]
    arr = [[0]*N for _ in range(M)]
    for i in point:
        arr[i[0]][i[1]] = 1
    n = DFS(arr)
    print(n)
