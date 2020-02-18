dr = [1,-1,0,0]
dc = [0,0,1,-1]

def point(G,N):
    global st
    for i in range(N):
        for j in range(N):
            if G[i][j] == 2:
                st = [i,j]

def DFS(st):
    ans = 0
    stack = []
    visit = []
    stack.append(st)
    while stack:
        r, c = stack.pop()
        visit.append([r,c])
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nc< 0 or nr> N-1 or nc>N-1 or maze[nr][nc] == 1:
                continue
            if [nr,nc] in visit:
                continue
            if maze[nr][nc] == 3:
                ans = 1
                return ans
            stack.append([nr,nc])
    return ans


T = int(input())
for t in range(1,T+1):
    N = int(input())
    maze = [list(map(int,list(input()))) for _ in range(N)]
    point(maze, N)
    print('#{} {}'.format(t, DFS(st)))