def DFS(k,stat):
    global MAX
    if k == 11:
        if MAX<stat:
            MAX = stat
        return
    if stat + (11 - k) * 100 <= MAX:
        return
    for i in range(11):
        if not visit[i] and arr[k][i]:
            visit[i] = 1
            stat += arr[k][i]
            DFS(k+1,stat)
            stat -= arr[k][i]
            visit[i]=0

T = int(input())
for t in range(1,T+1):
    arr = [list(map(int, input().split())) for _ in range(11)]
    visit = [0]*11
    MAX = 0
    DFS(0,0)
    print(MAX)