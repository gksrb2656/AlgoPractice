dp = [[1]*10]
for _ in range(99):
    dp.append([0]*10)
for i in range(1,100):
    for j in range(1,10):
        dp[i][0] = dp[i-1][1]
        if j == 9:
            dp[i][j] =  dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(dp)
N=int(input())
print(sum(dp[N-1][1:])%1000000000)
