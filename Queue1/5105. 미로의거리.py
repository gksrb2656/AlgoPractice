from collections import deque
dr = [1,0,-1,0]
dc = [0,1,0,-1]

for t in range(1,int(input())+1):
    N = int(input())
    maze = [list(map(int,list(input()))) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    def BFS():
        for i in range(N):
            for j in range(N):
                if maze[i][j] == 2:
                    Q = deque()
                    Q.append((i,j,0))
                    cnt = 0
                    while Q:
                        r, c, k  = Q.popleft()
                        for d in range(4):
                            nr = r + dr[d]
                            nc = c + dc[d]
                            if nr>N-1 or nc>N-1 or nr<0 or nc<0 or visit[nr][nc]:continue
                            if not maze[nr][nc]:
                                Q.append((nr,nc,k+1))
                                visit[nr][nc] = 1
                            elif maze[nr][nc] == 3:
                                return k
        return -1
    print("#{} {}".format(t, BFS()))