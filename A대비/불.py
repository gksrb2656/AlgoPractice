# from collections import deque
# dr = (1,0,-1,0)
# dc = (0,1,0,-1)
#
# def BFS():
#     n_s=1
#     while Q:
#         r,c,type,depth = Q.popleft()
#         for d in range(4):
#             nr, nc = r+dr[d],c+dc[d]
#             if arr[nr][nc] =='.':
#                 if type =='*':
#                     arr[nr][nc] = type
#                     Q.append((nr,nc,type,depth+1))
#                 else:
#                     if nr==N or nr==1 or nc==M or nc==1:
#                         return depth+1
#                     if not visit[nr][nc]:
#                         Q.append((nr,nc,type,depth+1))
#                         visit[nr][nc] = 1
#                         n_s+=1
#                     else:
#                         n_s -= 1
#         if n_s == 0:
#             return "IMPOSSIBLE"
#     return "IMPOSSIBLE"
#
#
# T = int(input())
# for t in range(1,T+1):
#     M, N = map(int, input().split())
#     arr = [['#']*(M+2)]
#     for _ in range(N):
#         arr.append(['#']+list(input())+['#'])
#     arr.append(['#']*(M+2))
#     visit = [[0]*(M+2) for _ in range(N+2)]
#     Q = deque()
#     for i in range(1,N+1):
#         for j in range(1,M+1):
#             if arr[i][j] =='@':
#                 s_r, s_c = i,j
#                 visit[i][j] = 1
#             elif arr[i][j] =='*':
#                 Q.append((i, j, '*', 1))
#     Q.append((s_r, s_c,'@',1))
#     if s_r==1 or s_r==N or s_c==1 or s_c==M:
#         print(1)
#     else:
#         print(BFS())