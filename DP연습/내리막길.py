import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*M for _ in range(N)]
dp[N-1][M-1] = 1
dr = (1,0,-1,0)
dc = (0,1,0,-1)
path_n = 0
def DFS(r,c):
    global path_n
    if (r,c) == (N-1,M-1):
        return dp[r][c]
    if dp[r][c]>=0:
        return dp[r][c]
    dp[r][c] = 0
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if nr > N - 1 or nc > M - 1 or nr < 0 or nc < 0: continue
        if arr[nr][nc] >= arr[r][c]: continue
        dp[r][c] += DFS(nr,nc)
    return dp[r][c]
DFS(0,0)
print(dp[0][0])
