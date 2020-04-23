from collections import deque
dr = [1,0,-1,0,1,-1,1,-1]
dc = [0,1,0,-1,-1,-1,1,1]

for t in range(1,int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(10)]
    visit = [[0]*10 for _ in range(10)]
    Q = deque()
    ans = 0
    for i in range(10):
        for j in range(10):
            if visit[i][j] or not arr[i][j]:continue
            ans += 1
            visit[i][j] = 1
            Q.append((i,j))
            while Q:
                r, c = Q.popleft()
                for d in range(8):
                    nr, nc = r+dr[d],c+dc[d]
                    if nr>9 or nc>9 or nr<0 or nc<0 or visit[nr][nc] or not arr[nr][nc]:continue
                    Q.append((nr,nc))
                    visit[nr][nc] = 1
    print("#{} {}".format(t,ans))
