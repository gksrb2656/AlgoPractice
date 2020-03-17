from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]

def BFS(t):
    global MIN
    Q = deque()
    MAX_k = 0
    visit_copy = [data[:] for data in visit]
    for i in combo:
        Q.append((i[0],i[1],0))
        visit_copy[i[0]][i[1]] = 1
    while Q:
        r,c,depth = Q.popleft()
        for d in range(4):
            nr = r+dr[d]
            nc = c+dc[d]
            if arr[nr][nc] == 1 or visit_copy[nr][nc]:continue
            visit_copy[nr][nc] = depth+1
            if not arr[nr][nc]:
                t -= 1
            if depth+1>MAX_k:
                MAX_k = depth+1
            if t==0:
                if MAX_k<MIN:
                    MIN = MAX_k
                return
            Q.append((nr, nc, depth + 1))

def comb(n, k):
    global total
    if k == M:
        BFS(total)
        return

    for i in range(n,len(viruses)):
        combo.append(viruses[i])
        comb(i+1,k+1)
        combo.pop()

N, M = map(int,input().split())
arr = [[1]*(N+2)]
for i in range(N):
    arr.append([1]+list(map(int, input().split())) + [1])
arr.append([1]*(N+2))
visit = [[0]*(N+2) for _ in range(N+2)]
viruses = []
total = 0
MIN = N*N
for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == 2:
            viruses.append((i,j))
        if not arr[i][j]:
            total += 1

combo = []
if total == 0:
    print(0)
else:
    comb(0,0)
    if MIN<N*N:
        print(MIN)
    else:
        print(-1)