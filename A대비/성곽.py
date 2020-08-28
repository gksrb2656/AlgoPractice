dir = {1:(0,-1), 2:(-1,0), 4:(0,1), 8:(1,0)}
def DFS(r,c,cnt):
    global r_v
    for d in (1,2,4,8):
        if not arr[r][c]&d:
            nr = r+dir[d][0]
            nc = c+dir[d][1]
            if visit[nr][nc] == -1:
                r_v += 1
                visit[nr][nc] = cnt
                DFS(nr, nc, cnt)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visit = [[-1]*N for _ in range(M)]
room_volume = []
cnt = -1
for i in range(M):
    for j in range(N):
        if visit[i][j]==-1:
            r_v = 1
            cnt += 1
            visit[i][j] = cnt
            DFS(i,j,cnt)
            room_volume.append(r_v)

dr = (1,0,-1,0)
dc = (0,1,0,-1)
room_expand = set()
for i in range(M):
    for j in range(N):
        for d in range(4):
            r = i+dr[d]
            c = j+dc[d]
            if r>M-1 or r<0 or c>N-1 or c<0:continue
            if visit[r][c] != visit[i][j]:
                room_expand.add(room_volume[visit[r][c]]+room_volume[visit[i][j]])
print(len(room_volume))
print(max(room_volume))
print(max(room_expand))
