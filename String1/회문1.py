for t in range(1, 11):
    N = int(input())
    li = [list(input()) for _ in range(8)]
    cnt = 0
    for i in range(8):
        r = ''
        c = ''
        for j in range(8-N+1):
            r = ''
            c = ''
            for k in range(N):
                if li[i][k+j] == li[i][N-k+j-1]:
                    r += li[i][k+j]
                if li[k+j][i] == li[N-k+j-1][i]:
                    c += li[k+j][i]
            if len(r) == N:
                cnt += 1
            if len(c) == N:
                cnt += 1
    print(cnt)