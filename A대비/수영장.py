def DFS(sum_p,n):
    global ans
    if n >= 12:
        if ans>sum_p:
            ans = sum_p
        return
    DFS(sum_p+prices[0]*plan[n],n+1)
    DFS(sum_p+prices[1],n+1)
    DFS(sum_p+prices[2],n+3)
    DFS(sum_p+prices[3],n+12)


T = int(input())
for t in range(1,T+1):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    ans = 3000*12
    DFS(0,0)
    print(ans)
