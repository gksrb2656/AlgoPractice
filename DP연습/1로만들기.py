N = int(input())

dp = [0]*(N+1)
dp[N] = 1
for i in range(N,-1,-1):
    if dp[i]:
        if not i%3:
            if not dp[i//3]:
                dp[i//3] = dp[i] + 1
            elif dp[i] + 1<dp[i//3]:
                dp[i//3] = dp[i] + 1
        if not i%2:
            if not dp[i//2]:
                dp[i//2] = dp[i] + 1
            elif dp[i] + 1<dp[i//2]:
                dp[i//2] = dp[i] + 1
        if not dp[i-1]:
            dp[i-1] = dp[i] + 1
        elif dp[i-1]>dp[i]+1:
            dp[i-1] = dp[i] + 1
        if dp[1]:
            break
print(dp[1]-1)