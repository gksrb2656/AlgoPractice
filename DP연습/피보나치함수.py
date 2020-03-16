'''
1 0 1 1 2 3
0 1 1 2 3 5
'''

T = int(input())
dp = [[0]*41 for _ in range(2)]
dp[0][0] = 1
dp[1][1] = 1
for t in range(1,T+1):
    N = int(input())
    for i in range(2,N+1):
        dp[0][i] = dp[0][i-2]+dp[0][i-1]
        dp[1][i] = dp[1][i - 2] + dp[1][i - 1]
    print(dp[0][N],dp[1][N])

