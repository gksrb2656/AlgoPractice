dp =[0]*91
dp[1] = 1
dp[2] = 1
dp[3] = 2

N = int(input())
for i in range(4,N+1):
    dp[i] = dp[i-2]+dp[i-1]
print(dp[N])