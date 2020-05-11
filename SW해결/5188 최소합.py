# from collections import deque
# dr = [1,0]
# dc = [0,1]
#
# for t in range(1, int(input())+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     Q = deque()
#     dp = [[0]*N for _ in range(N)]
#     dp[0][0] = arr[0][0]
#     Q.append((0,0))
#     while Q:
#         r, c = Q.popleft()
#         for d in range(2):
#             nr = r + dr[d]
#             nc = c + dc[d]
#             if nr>N-1 or nc>N-1:continue
#             if not dp[nr][nc] or arr[nr][nc] + dp[r][c] < dp[nr][nc]:
#                 Q.append((nr,nc))
#                 dp[nr][nc] = arr[nr][nc]+dp[r][c]
#     print(dp[N-1][N-1])

# #동식이거
# def move_sum():
#     global N, board
#     for r in range(N):
#         for c in range(N):
#             value=[]
#             for nr,nc in (r-1,c),(r,c-1):
#                 if not (0<=nr<N and 0<=nc<N): continue
#                 value.append(board[nr][nc])
#             if value:
#                 board[r][c] += min(value)
#
# T = int(input())
# for tc in range(1,1+T):
#     N = int(input())
#     board = [0]*N
#     for i in range(N):
#         board[i] = list(map(int, input().split()))
#
#     move_sum()
#     print('#{} {}'.format(tc, board[N-1][N-1]))

# #교수님거
# # 교수님 dfs
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     MAP = [list(map(int, input().split())) for _ in range(N)]
#
#     ans = 0xffffff
#
#
#     def dfs(x, y, d):
#         global ans
#         if d >= ans: return
#         if x == N - 1 and y == N - 1:
#             ans = min(ans, d)
#             return
#         if x + 1 < N:
#             dfs(x + 1, y, d + MAP[x + 1][y])
#         if y + 1 < N:
#             dfs(x, y + 1, d + MAP[x][y + 1])
#
#
#     dfs(0, 0, MAP[0][0])
#     print("#{} {}".format(tc, ans))
#
#
# # 교수님 dp memoization?
# for tc in range(1,int(input())+1):
#     N = int(input())
#     MAP = [list(map(int, input().split())) for _ in range(N)]
#     D=[[0]*N for _ in range(N)]
#
#     def solve(x, y):
#         if x == 0 and y == 0:
#             return MAP[0][0]
#         if D[x][y] : return D[x][y]
#
#         a = b = 0xffffff
#         if x > 0: # 위에서 오는 경우
#             a = solve(x-1, y)+MAP[x][y]
#
#         if y > 0:  # 왼쪽에서 오는 경우
#             b = solve(x, y-1)+MAP[x][y]
#
#         D[x][y] = min(a, b)
#         return D[x][y]
#
#     print("#{} {}".format(tc, solve(N-1, N-1)))
#
# # 교수님 반복
# for tc in range(1,int(input())+1):
#     N = int(input())
#     MAP = [list(map(int, input().split())) for _ in range(N)]
#
#     def solve2():
#         memo = [[0]*N for _ in range(N)]
#         memo[0][0] = MAP[0][0]
#
#         for i in range(1,N):
#             memo[0][i] = memo[0][i-1] + MAP[0][i]
#             memo[i][0] = memo[i-1][0] + MAP[i][0]
#
#         for i in range(1,N):
#             for j in range(1,N):
#                 memo[i][j] = min(memo[i-1][j],memo[i][j-1])+MAP[i][j]
#
#         return memo[N-1][N-1]
#     print('#{} {}'.format(tc,solve2()))