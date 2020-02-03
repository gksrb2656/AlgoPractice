T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    li = [list(input()) for i in range(N)]
    li2 = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            li2[i][j] = li[j][i]
    if N == M:
        for k in range(N):
            if li[k] == li[k].reverse():
                print(li[k])
            elif li2[k] == li2[k].reverse():
                print(li2[k])
    else:
        for k in range(N-M-1)