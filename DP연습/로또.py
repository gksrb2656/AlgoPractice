T = int(input())
for t in range(1,T+1):
    N, M =map(int,input().split())
    dp = [[0]*(M+1) for _ in range(N+1)]
    for i in range(0,M+1):
        dp[1][i] = i

    for i in range(2,N+1):
        for j in range(2,M+1):
            # dp[i][0] = 0
            dp[i][j] = dp[i-1][j//2]+dp[i][j-1]
    print(dp[N][M])

# for _ in range(int(input())):
#
#     N, M = map(int, input().split())
#     result = 0
#     li = [0] * N
#     cnt = 0
#     for i in range(N):
#         li[i] = [0] * (M + 1)
#
#     if N != 1:
#         for i in range(1, (M // (2 ** (N - 1))) + 1):
#             li[cnt][i] += 1
#
#         while 1:
#             cnt += 1
#             if cnt == N-1:
#                 break
#
#             for i in range(2 * (cnt - 1), len(li[cnt - 1])):
#                 if li[cnt - 1][i] != 0:
#                     num = li[cnt - 1][i]
#                     for j in range(2 * i, M // (2 ** (N - cnt - 1)) + 1):
#                         li[cnt][j] += num
#
#         for i in range(len(li[cnt - 1])):
#             if li[cnt - 1][i] != 0:
#                 result += ((M - 2 * i) + 1) * li[cnt-1][i]
#                 print(result)
#     else:
#         result = M
#
#     print(int(result))
#     for jj in li:
#         print(jj)