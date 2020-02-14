T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print('#{}'.format(t))
    for i in range(3):
        for j in range(N):
            print(arr[N-j-1][i], end = '')
        print(' ', end='')
        for k in range(N):
            print(arr[N-i-1][N-k-1], end = '')
        print(' ', end='')
        for l in range(N):
            print(arr[l][N-i-1], end = '')
        print()
