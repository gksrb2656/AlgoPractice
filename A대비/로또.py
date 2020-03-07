import sys
sys.setrecursionlimit(10**6)
def divide(i,j):
    global d
    if (j + 1) % 2 and j:
        if visit[i][j // 2] == 0:
            d += 1
            divide(i,j//2)


T = int(input())
for t in range(1,T+1):
    N, M =map(int,input().split())
    if N>1:
        MAX = int(M**(1/(2*(N-1))))
        visit = [[0]*(M+1) for _ in range(MAX+1)]
        cnt = 1
        if N==0 or 1 * (2 ** (N-1)) > M:
            cnt = 0
        else:
            for i in range(1, MAX + 1):
                for j in range(1,N):
                    visit[i][i*(2**j)] = 1
        if cnt:
            for i in range(1,MAX+1):
                n = 1
                for j in range(i*(2**(N-1)),M+1):
                    d = 0
                    divide(i,j)
                    n += d
                    if visit[i][j] == 0:
                        visit[i][j] = 1
                        cnt += n
    else:
        cnt = M
    print(cnt)

# def lotto(k,n):
#     global cnt
#     if k == N:
#         cnt += 1
#         return
#     if n>M:
#         return
#
#     for i in range(n,M+1):
#         lotto(k+1,i*2)
#
# T = int(input())
# for t in range(1,T+1):
#     N, M =map(int,input().split())
#     cnt = 0
#     lotto(0,1)
#     print(cnt)