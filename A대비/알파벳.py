# # from collections import deque
# #
# # dr = [1,-1,0,0]
# # dc = [0,0,1,-1]
# #
# # R, C = map(int,input().split())
# # arr = [list(input()) for _ in range(R)]
# # Q = deque()
# # Q.append((0,0,arr[0][0],1))
# # Max = 0
# # while Q:
# #     r,c,s,cnt = Q.pop()
# #     if cnt>Max:
# #         Max = cnt
# #     for d in range(4):
# #         nr,nc = r+dr[d], c+dc[d]
# #         if nr>R-1 or nc>C-1 or nr<0 or nc<0:continue
# #         if arr[nr][nc] in s:continue
# #         Q.append((nr,nc,s+arr[nr][nc],cnt+1))
# # print(Max)
#
# import sys
# def BFS(x, y):
#     global answer
#     q = set([(x, y, board[x][y])])
#
#     while q:
#         x, y, ans = q.pop()
#
#         # 좌우상하 갈 수 있는지 살펴본다
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             # index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크한다
#             if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
#                 q.add((nx,ny,ans + board[nx][ny]))
#                 answer = max(answer, len(ans)+1)
#
#
# R, C = map(int, sys.stdin.readline().split())
# board = [list(sys.stdin.readline().strip()) for _ in range(R)]
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
#
# answer = 1
# BFS(0, 0)
# print(answer)
