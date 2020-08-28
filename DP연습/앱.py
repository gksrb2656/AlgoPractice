# N, M = map(int, input().split())
# memory = list(map(int, input().split()))
# cost = list(map(int, input().split()))
# s_cost = sum(cost)
# dp = [-1]*(s_cost+1)
# dp[0] = 0
# for i in range(N):
#     for j in range(s_cost - cost[i] - 1, -1, -1):  # 최대시간에서 줄여가며
#         if dp[j] != -1:  # 이전에 만들었던 값이 있다면
#             dp[j + cost[i]] = max(dp[j + cost[i]], dp[j] + memory[i])
#
# for i in range(s_cost):
#     if dp[i] >= M:  # 가장 작게 드는 비용을 찾았다면 출력
#         print(i)
#         break
# #
# def DFS(c,idx):
#     if idx==N:
#         return 0
#
#     if memo[idx][c]>=0:
#         return memo[idx][c]
#
#     ret = DFS(c,idx+1)
#     if c>cost[idx]:
#         ret = max(DFS(c-cost[idx],idx+1)+memory[idx], ret)
#     memo[idx][c] = ret
#     return ret
#
# N, M = map(int, input().split())
# memory = list(map(int, input().split()))
# cost = list(map(int, input().split()))
# visit = [0]*N
# s_cost = sum(cost)
# memo = [[-1]*(s_cost+1) for _ in range(N+1)]
# for i in range(s_cost+1):
#     memo[0][i] = 0
# for c in range(s_cost):
#     if DFS(c,0)>=M:
#         print(c)
#     break


import sys

def solve(here, left):
    if here == memory_num:
        return 0
    ret = dp[here][left]
    if ret != -1:
        return ret

    ret = solve(here + 1, left)

    if left >= costs[here]:
        ret = max(ret, memories[here] + solve(here + 1, left - costs[here]))

    dp[here][left] = ret

    return ret


memory_num, memory_needed = map(int, sys.stdin.readline().strip().split())
memories = tuple(map(int, sys.stdin.readline().strip().split()))
costs = tuple(map(int, sys.stdin.readline().strip().split()))

dp = [[-1] * 10000 for _ in range(memory_num)]

for i in range(10000):
    if solve(0, i) >= memory_needed:
        print(i)
        break