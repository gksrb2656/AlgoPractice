N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

def dfs(visit, v):
    visit.append(v)
    for i in range(N):
        if arr[v][i] == 1 and i not in visit:
            visit.append(i)
            dfs(visit, i)

        if i == N-1:
            for j in range(1,len(visit)):
                arr[visit[0]][visit[j]] = 1
            return

for i in range(N):
    dfs([],i)
for i in range(N):
    for j in range(i+1,N):
        if arr[i][j] == 1 and arr[j][i] == 1:
            arr[i][i] = 1
            arr[j][j] = 1
for i in arr:
    print(*i)



