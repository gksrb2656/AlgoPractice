N = int(input())
wine = [0] * N
for i in range(N):
    wine[i] = int(input())

dp = [0]*N

for i in range(N):
    if i == 0:
        dp[0]=wine[0]a
    elif i == 1:
        dp[1] = wine[0]+wine[1]
    else:
        dp[i] = max(dp[i - 3] + wine[i-1]+wine[i], dp[i - 2] + wine[i], wine[i - 1], dp[i - 1])
print(dp[-1])
