dp = [[0,0] for _ in range(80)]
dp[0][0] = 1
dp[1][0] = 1
dp[0][1] = 4
dp[1][1] = 6
for i in range(2,80):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1]+dp[i][0]*2
def solution(N):
    answer = dp[N-1][1]
    return answer