from collections import deque
# import sys
# sys.setrecursionlimit(10**6)
#
# dr = [0,1,0,-1]
# dc = [1,0,-1,0]
#
# def Melting(k,total):
#     global time
#     visit_b = [[0] * M for _ in range(N)]
#
#     BFS(k,visit_b)
#     for i in range(N):
#         for j in range(M):
#             if melt_b[i][j]==k:
#                 cheese[i][j] = 0
#                 total -= 1
#     if total != 0:
#         Melting(k+1,total)
#         cheese_num.append(total)
#     else:
#         time = k
#         return
#
#
# def BFS(k,visit_b):
#     Q.append((0,0))
#     while Q:
#         r, c = Q.popleft()
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if nr>N-1 or nc>M-1 or nr<0 or nc<0:
#                 continue
#             if cheese[nr][nc]:
#                 melt_b[nr][nc] = k
#             elif not visit_b[nr][nc]:
#                 Q.append((nr,nc))
#                 visit_b[nr][nc] = 1
#
# N, M = map(int, input().split())
# cheese = [list(map(int, input().split())) for _ in range(N)]
# melt_b = [[0]*M for _ in range(N)]
# Q = deque()
# total = 0
# time = 0
# cheese_num = []
# for i in range(N):
#     for j in range(M):
#         if cheese[i][j]:
#             total += 1
# Melting(1,total)
# print(time)
# if cheese_num:
#     print(cheese_num[0])
# else:
#     print(total)

##DFS##
# import sys
# sys.setrecursionlimit(1000000)
#
# dr = [1,0,-1,0]
# dc = [0,1,0,-1]
# def DFS(r,c):
#     for d in range(4):
#         nr = r+dr[d]
#         nc = c+dc[d]
#         if nr>N-1 or nc>M-1 or nr<0 or nc<0 or arr[nr][nc] or visit[nr][nc]:continue
#         visit[nr][nc] = 1
#         DFS(nr,nc)
#
# def melt(r, c):
#     global total, cnt, flag
#     if not total:
#         return
#     for d in range(4):
#         nr = r + dr[d]
#         nc = c + dc[d]
#         if nr > N - 1 or nc > M - 1 or nr < 0 or nc < 0: continue
#         if visit[nr][nc] == 1:
#             visit[nr][nc] = 0
#             melt(nr, nc)
#         elif arr[nr][nc]:
#             total -= 1
#             arr[nr][nc] = 0
#             if total == 0:
#                 flag = True
#                 return
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# total = 0
# cnt = 0
# remain = []
# visit = [[0] * M for _ in range(N)]
# for i in range(N):
#     for j in range(M):
#         if arr[i][j]:
#             total += 1
#
# flag = False
# last = total
# while not flag:
#     cnt += 1
#     DFS(0, 0)
#     melt(0, 0)
#     if total:
#         last = total
# print(cnt)
# print(last)


D = [(0,1),(0,-1),(1,0),(-1,0)] #동서남북

def melt(arr):
    global time,cheese
    print(len(arr))
    cheese -= len(arr) #일단 치즈 개수 감소
    print(cheese)
    if cheese:  #치즈가 남아있으면
        for x,y in arr:
            board[x][y] = 0 #다시 다 0으로 만들기
        return False
    else: #만약 치즈가 다 녹으면
        ans = len(arr) #방금까지 남아있던 치즈 개수 = ans
        return ans

def BFS():
    global time,cheese
    q = deque([(0,0)]) #젤 첨에 0,0으로 시작
    check = [[0] * C for _ in range(R)]  # 방문 리스트 BFS호출될때마다 초기화
    check[0][0] = 1 #방문 표시
    # print(time,'시간')
    melting = [] #녹일 좌표
    while q:
        r,c = q.popleft()
        for dr,dc in D: #동서남북 방향
            nr,nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and not check[nr][nc]: #보드 내부에 다음 좌표가 있고 방문 안했으면
                if board[nr][nc] == 0: #치즈가 없고 구멍이면
                    check[nr][nc] = 1 #방문표시
                    q.append((nr,nc)) #큐에 넣기
                    # print(r,c,nr,nc)
                elif board[nr][nc] > 0: #구멍이랑 접촉한 치즈면
                    check[nr][nc] = 1 #방문 표시
                    melting.append((nr,nc)) #녹일 좌표에 append
                    # print(r,c,nr,nc,'녹음')
    print(melting)
    if melt(melting):
        return True
    else:
        # for jj in board:
        #     print(jj)
        return False
    # if c == 0: #치즈 다 녹으면
    #     print(cheese) #그 전까지 남아있던 치즈 출력
    #     print(abs(time) + 1) #다 녹을때까지 걸린 시간 출력
    #     return True
    # else:
    #     cheese = min(cheese,c) #치즈가 녹아서 줄어든 수로 변경
    #     print(cheese,'치즈 개수')
    #     return False

R,C = map(int,input().split())
board = [];c = 0 #c는 치즈가 있는 칸의 최초 개수
for a in range(R):
    ls = list(map(int,input().split()))
    c += ls.count(1)
    board.append(ls) #치즈 판 입력
cheese = c #치즈조각 최초 개수
# print(cheese)

time = -1 #일단 한시간 뒤로 설정
while True:
    if BFS(): #함수 실행해서 치즈가 다 없어지면
        break #종료
    else: #아니면
        time -= 1 #한시간 더 추가하고 다시 반복