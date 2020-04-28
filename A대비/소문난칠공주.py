# def DFS(r,c,y_cnt,cnt,path):
#     if cnt == 7:
#         return
#
#     if r+1<4 and not visit[r+1][c]:
#         if class_room[r+1][c]=='S':
#             visit[r+1][c] = 1
#             DFS(r+1,c,y_cnt,cnt+1,path+[(r+1,c)])
#             visit[r+1][c]=0
#         elif class_room[r+1][c]=='Y':
#             if y_cnt<3:
#                 visit[r+1][c]=1
#                 DFS(r+1,c,y_cnt+1,cnt+1,path+[(r+1,c)])
#                 visit[r+1][c]=0
#     if c+1<4 and not visit[r][c+1]:
#         if class_room[r][c+1]=='S':
#             visit[r][c+1] = 1
#             DFS(r,c,y_cnt,cnt+1,path+[(r,c+1)])
#             visit[r][c+1] = 0
#         elif class_room[r][c+1]=='Y':
#             if y_cnt<3:
#                 visit[r][c+1] = 1
#                 DFS(r,c+1,y_cnt+1,cnt+1,path+[(r,c+1)])
#                 visit[r][c+1] = 0
#     if r-1>0 and not visit[r-1][c]:
#         if class_room[r-1][c]=='S':
#             visit[r-1][c] = 1
#             DFS(r,c,y_cnt,cnt+1,path+[(r-1,c)])
#             visit[r - 1][c] = 0
#         elif class_room[r-1][c]=='Y':
#             if y_cnt<3:
#                 visit[r - 1][c] = 1
#                 DFS(r,c,y_cnt+1,cnt+1,path+[(r-1,c)])
#                 visit[r - 1][c] = 0
#     if c-1>0 and not visit[r][c-1]:
#         if class_room[r][c-1]=='S':
#             visit[r-1][c] = 1
#             path.append
#             DFS(r,c,y_cnt,cnt+1,path+[(r-1,c)])
#             visit[r - 1][c] = 0
#         elif class_room[r-1][c]=='Y':
#             if y_cnt<3:
#                 visit[r - 1][c] = 1
#                 DFS(r,c,y_cnt+1,cnt+1,path+[(r-1,c)])
#                 visit[r - 1][c] = 0

from collections import deque

dr=[1,0,-1,0]
dc=[0,1,0,-1]

def combo(com,n,y_cnt,cnt):
    global ans
    if cnt == 7:
        ans += BFS(com)
    for i in range(n,25):
        r,c = i//5,i%5
        if class_room[r][c]=='Y':
            if y_cnt==3:continue
            combo(com+[(r,c)],i+1,y_cnt+1,cnt+1)
        else:
            combo(com+[(r,c)],i+1,y_cnt,cnt+1)

def BFS(path):
    Q=deque()
    visit = [path[0]]
    Q.append(path[0])
    while Q:
        r,c = Q.popleft()
        for d in range(4):
            nr = r+dr[d]
            nc = c+dc[d]
            if nr>4 or nc>4 or nr<0 or nc<0:continue
            if (nr,nc) in path:
                if (nr,nc) in visit:continue
                visit.append((nr,nc))
                Q.append((nr,nc))
    if len(visit)==7:
        return 1
    else:
        return 0

class_room = [list(input()) for _ in range(5)]
ans = 0
paths = []
combo([],0,0,0)
print(ans)