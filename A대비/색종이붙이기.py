# from copy import deepcopy
#
# def DFS(k):
#     global total
#     global ans
#     if k > ans:
#         return
#     if total == 0:
#         if ans > k:
#             ans = k
#     for i in range(10):
#         for j in range(10):
#             if arr[i][j]:
#                 break
#         if arr[i][j]:
#             break
#
#     for size in range(1,6):
#         if paper_num[size - 1] == 5:
#             continue
#         if paper_size(i,j,size):
#             paper_num[size-1] += 1
#             total -= (size**2)
#             for r in range(i, i + size):
#                 for c in range(j, j + size):
#                     arr[r][c] = 0
#             DFS(k+1)
#             total += size ** 2
#             paper_num[size - 1] -= 1
#             for r in range(i, i + size):
#                 for c in range(j, j + size):
#                     arr[r][c] = 1
#
# def paper_size(i, j, size):
#     for r in range(i, i + size):
#         for c in range(j, j + size):
#             if r > 9 or c > 9 or r < 0 or c < 0:
#                 return 0
#             if arr[r][c] != 1:
#                 return 0
#     return 1
#
# arr = [list(map(int, input().split())) for _ in range(10)]
# total = 0
# for i in range(10):
#     for j in range(10):
#         total += arr[i][j]
# paper_num = [0]*5
# ans = 25
# DFS(0)
# if ans == 25:
#     print(-1)
# else:
#     print(ans)

from copy import deepcopy


