from collections import deque

for t in range(1,int(input())+1):
    N, M = map(int, input().split())
    Q = deque()
    Q.append((N,0))
    ans = 0
    visit = [0]*2000001
    while Q:
        v, k = Q.popleft()
        if v == M:
            ans = k
            break
        if not visit[v+1] and v+1<=1000000:
            visit[v+1] = 1
            Q.append((v+1,k+1))
        if v-1 and not visit[v -1]:
            visit[v-1] = 1
            Q.append((v-1,k+1))
        if not visit[v*2] and v*2<=1000000:
            visit[v*2] = 1
            Q.append((v*2,k+1))
        if v-10 and not visit[v-10]:
            visit[v-10] = 1
            Q.append((v-10,k+1))
    print("#{} {}".format(t, ans))