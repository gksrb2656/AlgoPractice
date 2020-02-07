T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    Pari = [list(map(int, input().split())) for _ in range(N)]
    # Chae = [list(map(int, input().split())) for _ in range(M)]
    Max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            p = 0
            for k in range(M):
                for l in range(M):
                    p += Pari[i+k][j+l]
            if p > Max:
                Max = p
    print('#{} {}'.format(t, Max))

