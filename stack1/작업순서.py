def DFS(v):
    visit[v] = True
    for w in G[v]:
        if not visit[w]:
            DFS(w)

    S.append(v)


for tc in range(1, 11):
    V, E = map(int, input().split())

    G = [[] for i in range(V + 1)]
    visit = [False] * (V + 1)
    indeg = [0] * (V + 1)
    S = []

    arr = list(map(int, input().split()))
    for i in range(0, E):
        u, v = arr[i * 2], arr[i * 2 + 1]
        G[u].append(v)  # 유향 그래프
        indeg[v] += 1

    for i in range(1, V + 1):
        if indeg[i]: continue
        DFS(i)

    print('#{} '.format(tc), end='')
    print(*S[::-1])