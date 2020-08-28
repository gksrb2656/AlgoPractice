def DFS(idx, remain, cnt):
    global N,MIN
    remain -= 1
    if idx==N:
        if cnt<MIN:
            MIN = cnt
        return
    if cnt>MIN:
        return

    #배터리를 교환하고 다음으로
    DFS(idx+1, stops[idx],cnt+1)
    #배터리 교환 x
    if remain>0:
        DFS(idx+1, remain, cnt)
T = int(input())
for t in range(1,T+1):
    stops = list(map(int, input().split()))
    N = stops[0]
    MIN = 10000
    DFS(2,stops[1],0)
    print(MIN)

for t in range(1, int(input())+1):
    arr = list(map(int, input()))
    N = arr[0]

    dp = [0xfffff]*(N+1)
    for i in range(1,2+arr[1]):
        dp[i]=0

    for i in range(2,N):
        for j in range(i+1, i+arr[i]+1):
            if j>N:break
            if dp[j]>dp[i]+1:
                dp[j] = dp[i]+1

    print(dp[N])