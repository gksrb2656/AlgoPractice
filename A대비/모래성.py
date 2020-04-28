from collections import deque

dr = (1,0,-1,0,1,1,-1,-1)
dc = (0,1,0,-1,-1,1,-1,1)

def BFS():
    global ans
    while Q:
        r, c, depth = Q.popleft()
        for d in range(8):
            nr, nc = r+dr[d], c+dc[d]
            if nr>H-1 or nc>W-1 or nr<0 or nc<0:continue
            if arr[nr][nc]>=9 or check[nr][nc]:continue
            if arr[nr][nc]:
                arr[nr][nc] -= 1
                if not arr[nr][nc]:
                    check[nr][nc] = 1
                    Q.append((nr,nc,depth+1))
    ans = depth

H, W = map(int, input().split())
arr = [list(map(lambda x:int(x) if x.isnumeric() else 0, list(input()))) for _ in range(H)]
check = [[0]*W for _ in range(H)]
Q = deque()
for i in range(H):
    for j in range(W):
        if not arr[i][j]:
            Q.append((i,j,0))
            check[i][j] = 1
ans = 0
BFS()
print(ans)
