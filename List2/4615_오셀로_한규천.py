# # import sys
# # sys.stdin = open('input.txt', 'r')
# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     board = [[0 for _ in range(N)] for _ in range(N)]
#     board[N//2][N//2] = 2
#     board[N//2 - 1][N//2] = 1
#     board[N//2 - 1][N//2 - 1] = 2
#     board[N//2][N//2 - 1] = 1
#     black = 0
#     white = 0
#     for i in range(M):
#         c, r, color = map(int, input().split())
#         r -= 1
#         c -= 1
#         board[r][c] = color
#         if c < N-1:
#             c_m = c
#             while (board[r][c_m+1] != color):
#                 if (board[r][c_m+1] != 0):
#                     c_m += 1
#                     if c_m == N-1:
#                         if board[r][c_m] != color:
#                             c_m = c
#                         break
#                 else:
#                     c_m = c
#                     break
#             for change in range(c+1, c_m+1):
#                 board[r][change] = color
#         if c > 0:
#             c_m = c
#             while (board[r][c_m-1] != color) :
#                 if (board[r][c_m-1] != 0):
#                     c_m -= 1
#                     if c_m == 0:
#                         if board[r][c_m] != color:
#                             c_m = c
#                         break
#                 else:
#                     c_m = c
#                     break
#             for change in range(c_m, c):
#                 board[r][change] = color
#         if r < N-1:
#             r_m = r
#             while (board[r_m+1][c] != color):
#                 if (board[r_m+1][c] != 0):
#                     r_m += 1
#                     if r_m == N-1:
#                         if board[r_m][c] != color:
#                             r_m = r
#                         break
#                 else:
#                     r_m = r
#                     break
#             for change in range(r+1, r_m+1):
#                 board[change][c] = color
#         if r > 0:
#             r_m = r
#             while (board[r_m-1][c] != color):
#                 if (board[r_m - 1][c] != 0):
#                     r_m -= 1
#                     if r_m == 0:
#                         if board[r_m][c] != color:
#                             r_m = r
#                         break
#                 else:
#                     r_m = r
#                     break
#             for change in range(r_m, r):
#                 board[change][c] = color
#         if c < N-1 and r < N-1:
#             r_m = r
#             c_m = c
#             while (board[r_m+1][c_m+1] != color):
#                 if (board[r_m + 1][c_m + 1] != 0):
#                     r_m += 1
#                     c_m += 1
#                     if (r_m == N-1) or (c_m == N-1):
#                         if board[r_m][c_m] != color:
#                             r_m = r
#                             c_m = c
#                         break
#                 else:
#                     r_m = r
#                     break
#             for change in range(1, (r_m - r+1)):
#                 board[r+change][c+change] = color
#         if c < N-1 and r > 0:
#             r_m = r
#             c_m = c
#             while (board[r_m-1][c_m+1] != color):
#                 if (board[r_m - 1][c_m + 1] != 0):
#                     r_m -= 1
#                     c_m += 1
#                     if (r_m == 0) or (c_m == N-1):
#                         if board[r_m][c_m] != color:
#                             r_m = r
#                             c_m = c
#                         break
#                 else:
#                     r = r_m
#                     break
#             for change in range(1, (r - r_m +1)):
#                 board[r-change][c+change] = color
#         if c > 0 and r < N-1:
#             r_m = r
#             c_m = c
#             while (board[r_m+1][c_m-1] != color):
#                 if (board[r_m+1][c_m-1] != 0):
#                     r_m += 1
#                     c_m -= 1
#                     if (r_m == N-1) or (c_m == 0):
#                         if board[r_m][c_m] != color:
#                             r_m = r
#                             c_m = c
#                         break
#                 else:
#                     r_m = r
#                     break
#             for change in range(1, (r_m - r+1)):
#                 board[r+change][c-change] = color
#         if c > 0 and r > 0:
#             r_m = r
#             c_m = c
#             while (board[r_m-1][c_m-1] != color):
#                 if (board[r_m-1][c_m-1] != 0):
#                     r_m -= 1
#                     c_m -= 1
#                     if (r_m == 0) or (c_m == 0):
#                         if board[r_m][c_m] != color:
#                             r_m = r
#                             c_m = c
#                         break
#                 else:
#                     r_m = r
#                     break
#             for change in range(1, (r - r_m + 1)):
#                 board[r - change][c - change] = color
#     for row in range(N):
#         for col in range(N):
#             if board[row][col] == 1:
#                 black += 1
#             elif board[row][col] == 2:
#                 white += 1
#     print('#{} {} {}'.format(t, black, white))
