def DFS(depth, start_t):
    global ans
    ans = max(ans,depth)
    for i in range(start_t,25):
        for j in range(start_t+1,25):
            if time_table[i][j]:
                DFS(depth+1,j)

for t in range(1,int(input())+1):
    N = int(input())
    time_table = [[0]*25 for _ in range(25)]
    start_t = 25
    for _ in range(N):
        st, ed = map(int, input().split())
        time_table[st][ed] = 1
        start_t = min(st,start_t)
    ans = 0
    DFS(0,start_t)
    print("#{} {}".format(t,ans))