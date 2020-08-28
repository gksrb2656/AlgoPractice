from collections import deque

dr = (1,0,-1,0)
dc = (0,1,0,-1)

def combo(depth):
    if depth==2:
        visit = [[[0, 0] for _ in range(N)] for _ in range(N)]
        BFS(st,visit)
        return

    for i in range(len(st_points)):
        if point_check[i]:continue
        point_check[i] = 1
        st.append([depth]+st_points[i])
        combo(depth+1)
        st.pop()
        point_check[i]=0

def BFS(points,visit):
    global MIN_t

    Q= deque()
    for s in points:
        Q.append(s+[1])
        n, i, j = s
        visit[i][j][n] = 1
    while Q:
        num,r,c,time = Q.popleft()
        if time+1>=MIN_t:
            return
        for d in range(4):
            nr = r+dr[d]
            nc = c+dc[d]
            if nr>N-1 or nc>N-1 or nr<0 or nc<0:continue
            if visit[nr][nc][num]:continue
            if visit[nr][nc][num^1]:
                MIN_t = min(MIN_t,time+1)
                return
            visit[nr][nc][num] = time+1
            Q.append((num,nr,nc,time+1))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
st_points = []
MIN_t = N*N
for i in range(N):
    for j in range(N):
        if arr[i][j]==2:
            st_points.append([i,j])

point_check = [0]*(len(st_points))
st = []
combo(0)
print(MIN_t-1)

