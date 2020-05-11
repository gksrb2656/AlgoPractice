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

memo = [0] * 100

#
# N, K = map(int, input().split())
# coins = set()
# for i in range(N):
#     coins.add(int(input()))
# coin = sorted(list(coins))
# def coinChange(n):
#     if n == 0:
#         return 0
#     if memo[n]:
#         return memo[n]
#
#     MIN = 0xfffff
#     for i in range(len(coin)):
#         if coin[i] > n:
#             continue
#
#         ret = coinChange(n - coin[i]) + 1
#         MIN = min(MIN, ret)
#
#     memo[n] = MIN
#     return memo[n]
#
#
# print(coinChange(8))
# print(memo[1:9])

