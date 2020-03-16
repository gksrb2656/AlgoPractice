N, K = map(int, input().split())
coins = set()
for i in range(N):
    coins.add(int(input()))
coins = sorted(list(coins))

dp = [K+1]*(K+1)
dp[0] = 0
for i in coins:
    if i<K:
        for j in range(i,K+1):
            if dp[j-i]+1<dp[j]:
                dp[j] = dp[j-i]+1
if dp[K]>K:
    print(-1)
else:
    print(dp[K])
