import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for i in range(1,T+1):
    N = int(input())
    li = [[0 for i in range(10)] for j in range(10)]
    cnt = 0
    for j in range(N):
        l1, r1, l2, r2, c = list(map(int, input().split()))
        for k in range(l1, l2+1):
            for m in range(r1, r2+1):
                if li[k][m] != 0:
                    li[k][m] = 3
                else:
                    li[k][m] = c
    for r1 in range(10):
        for r2 in range(10):
            if li[r1][r2] == 3:
                cnt += 1
    print('#{0} {1}'.format(i, cnt))
