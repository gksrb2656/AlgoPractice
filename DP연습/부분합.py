import sys;input=sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int,input().split()))
dp = [0]*N
dp[0]=arr[0]
min_ans = 10**9
ans = 1
if dp[0]>=S:
    min_ans = 1
else:
    min_ans = 1
    for i in range(1,N):
        if arr[i]>=S:
            min_ans = 1
            break
        ans += 1
        dp[i] = dp[i-1]+arr[i]
        if dp[i]>S:
            s = dp[i]
            flag = 1
            while flag and ans>1:
                s -= arr[i-(ans-1)]
                if s>=S:
                    ans -= 1
                    dp[i] = s
                else:
                    flag = 0
            min_ans = min(ans,min_ans)
if min_ans>N:
    print(0)
else:
    print(min_ans)