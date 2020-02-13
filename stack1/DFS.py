
def dfs(visited, V):
    print(V, end =" ")
    for i in range(1, N+1):
        if arr[V][i] == 1 and i not in visited:
            visited.append(i)
            dfs(visited, i)

N, M = map(int, input().split())

arr = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    st, ed = map(int, input().split())
    arr[st][ed] = arr[ed][st] = 1

dfs([1], 1)