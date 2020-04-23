from collections import deque

def s_path():
    while Q:
        node, path = Q.popleft()
        for i in range(N):
            if visit[i]:continue
            cnt = 0
            for k in range(K):
                if bits[node][k] != bits[i][k]:
                    cnt+=1
                if cnt>1:break
            if cnt > 1: continue
            if i == B-1:
                return path+[i]
            Q.append((i,path+[i]))
            visit[i] = 1
    return 0

N, K = map(int, input().split())
bits = [input() for _ in range(N)]
visit = [0]*N
Q = deque()
A, B = map(int, input().split())
Q.append((A-1,[A-1]))
visit[A-1] = 1

answer = s_path()
if answer:
    for i in answer:
        print(i+1, end=' ')
else:
    print(-1)