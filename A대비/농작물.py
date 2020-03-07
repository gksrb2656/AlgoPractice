T = int(input())
for t in range(1, T+1):
    N = int(input())
    Farm = [list(map(int,input())) for _ in range(N)]
    summ = 0
    for i in range(N//2+1):
        for j in range(N//2-i,N//2+i+1):
            summ += Farm[i][j]
    for i in range(1, N//2+1):
        for j in range(i,N-i):
            summ += Farm[N//2 + i][j]
    print('#{} {}'.format(t, summ))

