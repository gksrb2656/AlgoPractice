# T = int(input())
# for t in range(1 ,T+1):
#     N = int(input())
#     li = [[0 for i in range(N)] for j in range(N)]
#     idx = 0
#     for i in range(N//2):
#         for j in range(4):
#             for k in range(i, N-1-i):
#                 idx += 1
#                 if j == 0:
#                     li[i][k] = idx
#                 elif j == 1:
#                     li[k][N-1-i] = idx
#                 elif j == 2:
#                     li[N-1-i][N-k-1] = idx
#                 elif j == 3:
#                     li[N-k-1][i] = idx
#     if N % 2:
#         li[N//2][N//2] = N**2
#     print('#{}'.format(t))
#     for l in li:
#         ll = list(map(str, l))
#         print(' '.join(ll))

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#
#     arr = [[0]*N for _ in range(N)]
#
#     r = 0
#     c = -1
#     num = 1
#     dir = 1
#     K = N
#
#     while 1:
#         for k in range(K): #수평이동
#             c += dir
#             arr[r][c] = num
#             num += 1
#         K -= 1
#         if K == 0:
#             break
#
#         for k in range(K):#수직이동
#             r += dir
#             arr[r][c] = num
#             num += 1
#
#         dir *= -1
#
#     print('#{}'.format(tc))
#     for i in range(N):
#         for j in range(N):
#             print(arr[i][j], end=' ')
#         print()

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    dir = 0

    r=0
    c=0
    num = 1

    while(num <= N*N):
        arr[r][c] = num
        num += 1

        nr = r+dr[dir]
        nc = c+dc[dir]
        if nr >= 0 and nr < N and nc >= 0 and nc < N and arr[nr][nc] == 0:
            r = nr
            c = nc
        else:
            dir = (dir+1)%4 #자주 쓰는 모듈화 연산
            r += dr[dir]
            c += dc[dir]

    print("#{}".format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()

