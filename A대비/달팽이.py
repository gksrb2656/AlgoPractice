K, N = map(int, input().split())
li = [[0 for i in range(N)] for j in range(N)]
idx = 0
for i in range(N // 2):
    for j in range(4):
        for k in range(i, N - 1 - i):
            idx += 1
            if j == 0:
                li[i][k] = idx
            elif j == 1:
                li[k][N - 1 - i] = idx
            elif j == 2:
                li[N - 1 - i][N - k - 1] = idx
            elif j == 3:
                li[N - k - 1][i] = idx
if N % 2:
    li[N // 2][N // 2] = N ** 2
if K != 1:
    ro = [[0 for i in range(N)] for j in range(N)]
    if K == 2:
        for i in range(N):
            for j in range(N):
                ro[j][N - 1 - i] = li[i][j]
    if K == 3:
        for i in range(N):
            for j in range(N):
                ro[N - 1 - j][N - 1 - i] = li[i][j]
    if K == 4:
        for i in range(N):
            for j in range(N):
                ro[N - 1 - j][i] = li[i][j]
    for l in ro:
        ll = list(map(str, l))
        for l2 in ll:
            print("{:>5}".format(str(l2)), end=' ')
        print()
else:
    for l in li:
        ll = list(map(str, l))
        for l2 in ll:
            print("{:>5}".format(str(l2)), end=' ')
        print()