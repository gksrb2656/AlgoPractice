def DFS(v,cnt):
    global MAX
    for i in range(1,N+1):
        if node[v][i] == 1 and not visit[i]:
            cnt += 1
            visit[i] = 1
            DFS(i,cnt)
            visit[i] = 0
            cnt -= 1
    if MAX<cnt:
        MAX = cnt
    return

T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    node = [[0]*(N+1) for _ in range(N+1)]
    MAX = 0
    for _ in range(M):
        r,c = map(int, input().split())
        node[r][c] = 1
        node[c][r] = 1
    for i in range(1,N+1):
        visit = [0] * (N + 1)
        visit[i] = 1
        DFS(i,0)
    print("#{} {}".format(t,MAX+1))