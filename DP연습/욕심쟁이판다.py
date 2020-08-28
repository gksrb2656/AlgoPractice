import sys
sys.setrecursionlimit(10**6)

dr = (1,0,-1,0)
dc = (0,1,0,-1)

def DFS(r,c):
    global ans
    if dp[r][c]>=0:
        return dp[r][c]+1
    dp[r][c] = 0
    for d in range(4):
        nr,nc = r+dr[d],c+dc[d]
        if nr>N-1 or nc>N-1 or nr<0 or nc<0:continue
        if arr[nr][nc]<=arr[r][c]:continue
        s = DFS(nr,nc)
        if s>dp[r][c]:
            dp[r][c] = s
        ans = max(dp[r][c],ans)
    return dp[r][c]+1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*N for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        DFS(i,j)
print(ans+1)