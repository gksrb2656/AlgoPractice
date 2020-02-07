
# def del_zero_up(tile, N):
# #     if dir == 'up':
# #         for i in range(N):
# #             for j in range(N):
# #                 k = i
# #                 while (tile[k][j] == 0) and k<N-1:
# #                     if tile[k+1][j] != 0:
# #                         tile[i][j], tile[k+1][j] = tile[k+1][j], tile[i][j]
# #                         break
# #                     k += 1
# #         return tile

T = int(input())
def del_zero(tile, N, dir):
    if dir == 'up':
        for i in range(N):
            for j in range(N):
                k = i
                while (tile[k][j] == 0) and k<N-1:
                    if tile[k+1][j] != 0:
                        tile[i][j], tile[k+1][j] = tile[k+1][j], tile[i][j]
                        break
                    k += 1
    elif dir == 'down':
        for i in range(N,0,-1):
            for j in range(N):
                k = i-1
                while (tile[k][j] == 0) and k > 0:
                    if tile[k-1][j] != 0:
                        tile[i-1][j], tile[k-1][j] = tile[k-1][j], tile[i-1][j]
                        break
                    k -= 1
    elif dir == 'right':
        for i in range(N,0, -1):
            for j in range(N,):
                k = i-1
                while (tile[j][k] == 0) and k > 0:
                    if tile[j][k-1] != 0:
                        tile[j][i-1], tile[j][k - 1] = tile[j][k - 1], tile[j][i-1]
                        break
                    k -= 1
    elif dir == 'left':
        for i in range(N):
            for j in range(N):
                k = i
                while (tile[j][k] == 0) and k < N-1:
                    if tile[j][k + 1] != 0:
                        tile[j][i], tile[j][k + 1] = tile[j][k + 1], tile[j][i]
                        break
                    k += 1
    return tile

for t in range(1,T+1):
    N, dir = input().split()
    N = int(N)
    tile = [list(map(int, input().split())) for _ in range(N)]
    if dir == 'up':
        for i in range(1, N):
            tile = del_zero(tile, N, dir)
            for j in range(N):
                if tile[i][j] == tile[i-1][j]:
                    tile[i - 1][j], tile[i][j] = tile[i][j]*2, 0
    elif dir == 'down':
        for i in range(N-1,0, -1):
            tile = del_zero(tile, N, dir)
            for j in range(N):
                if tile[i-1][j] == tile[i][j]:
                    tile[i][j], tile[i-1][j] = tile[i-1][j]*2, 0
    elif dir == 'left':
        for i in range(1, N):
            tile = del_zero(tile, N, dir)
            for j in range(N):
                if tile[j][i] == tile[j][i-1]:
                    tile[j][i], tile[j][i-1] = tile[j][i-1]*2, 0
    else:
        for i in range(N-1,0,-1):
            tile = del_zero(tile, N, dir)
            for j in range(N):
                if tile[j][i-1] == tile[j][i]:
                    tile[j][i], tile[j][i-1] = tile[j][i-1]*2, 0
    print('#{}'.format(t))
    for i in tile:
        tt = list(map(str, i))
        print(' '.join(tt))






