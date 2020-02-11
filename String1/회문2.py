for t in range(1,11):
    T = int(input())
    li = [list(input()) for _ in range(100)]
    M = 100
    Max = 0
    while 1:
        for i in range(100):
            r = ''
            c = ''
            for j in range(100-M+1):
                r = ''
                c = ''
                for k in range(M):
                    if li[i][k+j] == li[i][M-k+j-1]:
                        r += li[i][k+j]
                    else:
                        break
                for k in range(M):
                    if li[k+j][i] == li[M-k+j-1][i]:
                        c += li[k+j][i]
                    else:
                        break
                if len(r) == M or len(c) == M:
                    break
            if len(r) == M or len(c) == M:
                break
        if len(r) == M or len(c) == M:
            break
        M -= 1
    print("#{} {}".format(t,M))


