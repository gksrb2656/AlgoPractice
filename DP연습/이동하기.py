from collections import deque
dr = [1,0]
dc = [0,1]

N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
dp = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            Q.append((i,j))
            dp[i][j] = arr[i][j]
            break
    if Q: break
while Q:
    r, c = Q.popleft()
    for d in range(2):
        nr = r + dr[d]
        nc = c + dc[d]
        if nr>N-1 or nc>M-1:continue
        sum_candy = 0
        if arr[nr][nc] + dp[r][c] > dp[nr][nc]:
            Q.append((nr,nc))
            dp[nr][nc] = arr[nr][nc]+dp[r][c]
print(dp[N-1][M-1])


# N, M = map(int, input().split())
# arr = [[0] * (M + 1)]
# for _ in range(N):
#     arr.append([0] + list(map(int, input().split())))
#
# for i in range(1, N + 1):
#     for j in range(1, M + 1):
#         arr[i][j] += max(arr[i - 1][j], arr[i][j - 1], arr[i - 1][j - 1])
# print(arr[N][M])
