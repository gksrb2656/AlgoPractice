from collections import deque
#
#
# MAX = 100001
#
#
# def solution(n, k):
#     q = deque([n])
#     visit = [0] * MAX
#
#     def nextPos(next, cur):
#         if 0 <= next and next < MAX:
#             if visit[next] == 0 or (visit[cur] + 1 < visit[next]):
#                 visit[next] = visit[cur] + 1
#                 q.append(next)
#
#     while q:
#         cur = q.popleft()
#         if cur == k:
#             return visit[cur]
#         nextPos(cur - 1, cur)
#         nextPos(cur + 1, cur)
#         nextPos(cur * 2, cur)
#
#
# if __name__ == "__main__":
#     N, K = map(int, input().split())
#     print(solution(N, K))
