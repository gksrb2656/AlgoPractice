from collections import deque

def BFS(r):
    Q = deque()
    Q.append((r,0))
    visit = [0]*(N+1)
    while Q:
        v,k = Q.popleft()
        value = k
        for i in range(1,N+1):
            if r==i:continue
            if arr[v][i] and not visit[i]:
                Q.append((i,k+1))
                visit[i] = 1
    return value

N = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]
m_score = 100000
while 1:
    r, c = map(int, input().split())
    if r == -1:
        break
    arr[r][c] = 1
    arr[c][r] = 1

candies = [0]*N
for i in range(1,N+1):
    candies[i-1] = BFS(i)

print(min(candies), candies.count(min(candies)))
for i in range(N):
    if candies[i] == min(candies):
        print(i+1, end = ' ')