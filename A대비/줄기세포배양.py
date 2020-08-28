from collections import deque
dr = [1,0,-1,0]
dc = [0,1,0,-1]

def BFS(T):
    global Q
    t = 0
    while t<T:
        q = list(Q)
        q.sort(reverse=True)
        Q = deque(q)
        for _ in range(len(Q)):
            k,r,c,state,time = Q.popleft()
            if state<k:
                Q.append((k,r,c,state+1,time+1))
                continue
            elif k<=state<2*k-1:
                Q.append((k,r,c,state+1,time+1))
            for d in range(4):
                nr,nc = r+dr[d], c+dc[d]
                if visit[K//2+nr][K//2+nc]:
                    continue
                visit[K//2 + nr][K//2 + nc] = k
                Q.append((k,nr,nc,0,time+1))
        t+=1
    return len(Q)

T = int(input())
for t in range(1,T+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*(M+K) for _ in range(N+K)]
    Q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                visit[i+K//2][j+K//2] = arr[i][j]
                Q.append((arr[i][j],i,j,0,0))
    print("#{} {}".format(t,BFS(K)))