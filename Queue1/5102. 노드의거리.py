from collections import deque

for t in range(1,int(input())+1):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        r, c = map(int, input().split())
        arr[r][c] = 1
        arr[c][r] = 1
    S, G = map(int, input().split())
    Q = deque()
    Q.append((S,0))
    visit = [0]*(V+1)
    def BFS():
        while Q:
            s, k = Q.popleft()
            for i in range(1,V+1):
                if arr[s][i] and not visit[i]:
                    if i==G:
                        return k+1
                    Q.append((i,k+1))
                    visit[i] = 1
        return 0
    print("#{} {}".format(t,BFS()))
