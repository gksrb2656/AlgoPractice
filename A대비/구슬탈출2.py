# from collections import deque
#
# dr = [1,-1,0,0]
# dc = [0,0,1,-1]
#
# N,M = map(int,input().split())
# arr = [list(input()) for _ in range(N)]
# visit = [[0]*M for _ in range(N)]
# Q = deque()
# Q2 = deque()
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 'R':
#             Q.append((i,j,'R',0))
#         elif arr[i][j] == 'B':
#             Q2.append((i,j,'B'))
#
# flag = False
# while Q:
#     r,c,type,k = Q.popleft()
#     if Q2:
#         r2,c2,type2 = Q2.popleft()
#     visit[r][c] = 1
#     arr[r][c] = '.'
#     for d in range(4):
#         nr = r+dr[d]
#         nc = c+dc[d]
#         nr2 = r2+dr[d]
#         nc2 = c2+dc[d]
#         if arr[nr2][nc2] == 'O':
#             k = -1
#             Q.clear()
#             break
#         if arr[nr][nc] == 'O':
#             flag = True
#             k += 1
#             Q.clear()
#             break
#         elif arr[nr][nc] == '.' and not visit[nr][nc]:
#             while arr[nr][nc] == '.':
#                 visit[nr][nc] = 1
#                 nr += dr[d]
#                 nc += dc[d]
#             if arr[nr][nc] == 'O':
#                 flag = True
#                 k+=1
#                 Q.clear()
#             else:
#                 arr[nr-dr[d]][nc-dc[d]] = 'R'
#                 Q.append((nr-dr[d],nc-dc[d],'R',k+1))
#             if arr[nr2][nc2] == '.':
#                 while arr[nr2][nc2] == '.':
#                     nr2 += dr[d]
#                     nc2 += dc[d]
#                 if arr[nr2][nc2] == 'O':
#                     k = -1
#                     Q.clear()
#                     break
#                 arr[r2][c2] = '.'
#                 arr[nr2 - dr[d]][nc2 - dc[d]] = 'B'
#                 Q2.append((nr2 - dr[d], nc2 - dc[d], 'B'))
#             else:
#                 Q2.append((r2, c2, 'B'))
#         elif arr[nr][nc] == 'B':
#             if arr[nr+dr[d]][nc+dc[d]] == '.' and not visit[nr+dr[d]][nc+dc[d]]:
#                 while arr[nr2][nc2] == '.':
#                     nr2 += dr[d]
#                     nc2 += dc[d]
#                 if arr[nr2][nc2] == 'O':
#                     k = -1
#                     Q.clear()
#                     break
#                 arr[r2][c2] = '.'
#                 arr[nr2 - dr[d]][nc2 - dc[d]] = 'B'
#                 Q2.append((nr2 - dr[d], nc2 - dc[d], 'B'))
#                 while arr[nr][nc] == '.':
#                     visit[nr][nc] = 1
#                     nr += dr[d]
#                     nc += dc[d]
#                 if arr[nr][nc] == 'O':
#                     flag = True
#                     k+=1
#                     Q.clear()
#                     break
#                 arr[nr-dr[d]][nc-dc[d]] = 'A'
#                 Q.append((nr - dr[d], nc - dc[d], 'R', k + 1))
#         if d == 3 and not Q:
#             for dd in range(4):
#                 nr2 = r2 +dr[dd]
#                 nc2= c2 +dc[dd]
#                 if arr[nr2][nc2] == '.' and not visit[nr2][nc2]:
#                     while arr[nr2][nc2] == '.':
#                         nr2 += dr[dd]
#                         nc2 += dc[dd]
#                     if arr[nr2][nc2] == 'O':
#                         k = -1
#                         Q.clear()
#                         break
#                     break
#             arr[r2][c2] = '.'
#             arr[nr2 - dr[dd]][nc2 - dc[dd]] = 'B'
#             Q2.append((nr2 - dr[dd], nc2 - dc[dd], 'B'))
#             Q.append((r,c,'R',k+1))
#             break
#     if k>10:
#         k = -1
#         break
#
# if flag:
#     print(k)
# else:
#     print(-1)

from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def BFS():
    while Q:
        r_r,r_c,b_r,b_c,k = Q.popleft()
        if k>10:
            break
        for d in range(4):
            nr_r,nr_c = r_r+dr[d],r_c+dc[d]
            nb_r, nb_c = b_r + dr[d], b_c + dc[d]
            cnt_r = 0
            while arr[nr_r][nr_c] !='#' and arr[nr_r][nr_c] !='O':
                nr_r += dr[d]
                nr_c += dc[d]
                cnt_r +=1
            cnt_b = 0
            while arr[nb_r][nb_c] != '#'and arr[nb_r][nb_c] != 'O':
                nb_r += dr[d]
                nb_c += dc[d]
                cnt_b+=1
            if arr[nb_r][nb_c] == 'O':
                continue
            if arr[nr_r][nr_c] == 'O':
                print(k)
                return
            if (nr_r, nr_c) == (nb_r, nb_c):
                if cnt_b > cnt_r:
                    nb_r -= dr[d]
                    nb_c -= dc[d]
                else:
                    nr_r -= dr[d]
                    nr_c -= dc[d]
            if nr_r-dr[d] != r_r or nr_c-dc[d] != r_c or nb_r-dr[d] != b_r or nb_c-dc[d] != b_c:
                if (nr_r-dr[d],nr_c-dc[d],nb_r-dr[d],nb_c-dc[d]) in visit: continue
                Q.append((nr_r-dr[d],nr_c-dc[d],nb_r-dr[d],nb_c-dc[d],k+1))
                visit.append((nr_r-dr[d],nr_c-dc[d],nb_r-dr[d],nb_c-dc[d]))
    print(-1)

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
visit = []
Q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            r_r,r_c = i,j
        elif arr[i][j] == 'B':
            b_r,b_c = i,j

Q.append((r_r,r_c,b_r,b_c,1))
visit.append((r_r,r_c,b_r,b_c))
BFS()


