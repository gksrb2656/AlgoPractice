from collections import deque

for t in range(1,int(input())+1):
    N, M = map(int, input().split())
    Q = deque(map(int, input().split()))
    Q.rotate(-M)
    print("#{} {}".format(t, Q.popleft()))