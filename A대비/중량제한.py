from collections import deque
import sys;input=sys.stdin.readline

def BFS(c):
    Q = deque()
    Q.append(st)
    visit = [0] * (N + 1)
    visit[st] = 1
    while Q:
        v = Q.popleft()
        for i,cc in arr[v]:
            if cc<c or visit[i]:continue
            if i == ed:
                return 1
            visit[i] = 1
            Q.append(i)
    return 0

def B_search():
    global min_c, max_c
    while min_c<=max_c:
        mid = (min_c+max_c)//2
        if BFS(mid):
            min_c = mid+1
        else:
            max_c = mid-1

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
min_c=max_c=0
for _ in range(M):
    A, B, C = map(int, input().split())
    if not min_c:min_c=C
    if not max_c:max_c=C
    arr[A].append((B,C))
    arr[B].append((A,C))
    min_c = min(min_c,C)
    max_c = max(max_c,C)

st, ed = map(int, input().split())

B_search()
print(max_c)
