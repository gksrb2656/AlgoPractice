from collections import deque

T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    pizzas = deque(map(int, input().split()))
    Q = deque()
    for i in range(N):
        Q.append((pizzas.popleft(),i+1))
    idx = N
    while Q:
        pizza, k = Q.popleft()
        pizza //= 2
        if pizza>0:
            Q.append((pizza, k))
        elif pizzas:
            idx += 1
            Q.append((pizzas.popleft(),idx))
        if len(Q) == 1:
            break
    print("#{} {}".format(t, Q.popleft()[1]))
