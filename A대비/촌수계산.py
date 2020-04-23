from collections import deque

N = int(input())
p1, p2 = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for t in range(int(input())):
    Parent, Baby = map(int, input().split())
    arr[Parent][Baby] = 1
    arr[Baby][Parent] = 1

Q = deque()
Q.append((p1,1))
visit = [0]*(N+1)
visit[p1] = 1
def BFS():
    while Q:
        p_idx, n = Q.popleft()
        for i in range(1,N+1):
            if arr[p_idx][i] and not visit[i]:
                if i == p2:
                    return n
                Q.append((i,n+1))
                visit[i] = 1
    return -1
print(BFS())