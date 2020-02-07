import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    li = [list(input()) for _ in range(N)]
    # print(li)
    for i in range(N):
        r = ''
        c = ''
        for j in range(N-M+1):
            r = ''
            c = ''
            for k in range(M):
                if li[i][k+j] == li[i][M-k+j-1]:
                    r += li[i][k+j]
                if li[k+j][i] == li[M-k+j-1][i]:
                    c += li[k+j][i]
            if len(r) == M:
                print('#{} {}'.format(t, r))
            elif len(c) == M:
                print('#{} {}'.format(t, c))