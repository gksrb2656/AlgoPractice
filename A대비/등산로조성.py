from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]

def BFS():
    global longest
    for i in high:
        Q.append(i)
    while Q:
        k,r,c = Q.popleft()
        if k > longest:
            longest = k
        visit[r][c] = 1
        for d in range(4):
            nr = r+dr[d]
            nc = c+dc[d]
            if nr>N-1 or nc>N-1 or nr<0 or nc<0:continue
            if MAP[r][c]>MAP[nr][nc]:
                Q.append((k+1,nr,nc))


def dig(i,j):
    for d in range(4):
        nr = i + dr[d]
        nc = j + dc[d]
        if nr > N - 1 or nc > N - 1 or nr < 0 or nc < 0: continue
        if visit[nr][nc] == 2: continue
        if MAP[nr][nc]>=MAP[i][j]:
            if MAP[nr][nc]>=MAP[i][j]:
                for s in range(K,0,-1):
                    if MAP[nr][nc] - s < MAP[i][j]:
                        visit[nr][nc] = 2
                        MAP[nr][nc] -= s
                        BFS()
                        MAP[nr][nc] += s
                    else:
                        break


T = int(input())
for t in range(1,T+1):
    N, K = map(int, input().split())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    high = []
    highst = 0
    for i in range(N):
        highst = max(highst,max(MAP[i]))
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == highst:
                high.append((1,i,j))
    visit = [[0]*N for _ in range(N)]
    Q = deque()
    longest = 0
    BFS()
    for i in range(N):
        for j in range(N):
            if visit[i][j] :
                dig(i,j)

    print("#{} {}".format(t,longest))
