from collections import deque

def BFS():
    global time, path
    flag = 0
    while Q:
        v,k = Q.popleft()
        visit[v] = 1
        if flag and k>time:
            return
        if v == K and not flag:
            flag = path = 1
            time = k
            continue
        elif v==K:
            path += 1
            continue
        for d in range(3):
            if d == 0:
                if v+1>100000 or visit[v+1]:continue
                Q.append((v+1,k+1))
            elif d==1:
                if v-1<0 or visit[v-1]:continue
                Q.append((v - 1, k + 1))
            elif d==2:
                if v*2>100000 or visit[2*v]:continue
                Q.append((v * 2, k + 1))

N, K = map(int, input().split())
visit = [0]*100001
visit[N]=[1]
time = 0
path = 0
Q = deque()
Q.append((N,0))
BFS()
print(time)
print(path)