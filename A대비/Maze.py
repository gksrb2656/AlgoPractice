import sys
sys.stdin = open('input.txt','r')
from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N =100
def BFS(maze, v):
    Q = deque()
    visit = list(v)
    Q.append(v)
    visit.append(v)
    global arrive
    # print(maze)
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr == 0 and nr == N - 1 and nc == 0 and nc == N - 1:
                continue
            if maze[nr][nc] != '1' and (nr, nc) not in visit:
                Q.append((nr,nc))
                visit.append((nr,nc))
            if maze[nr][nc] == '3':
                arrive = 1


for t in range(1, 11):
    arrive = 0
    T = int(input())
    maze = [input() for _ in range(N)]
    BFS(maze, (1,1))
    print(arrive)
    # r = 1
    # c = 1
    # i = -1
    # cnt = 0
    # arrive = 0
    # # for r in range(1,N):
    # #     for c in range(1,N):
    # while 1:
    #     i += 1
    #     i = i%4
    #     if cnt >= 4:
    #         break
    #     while 1:
    #         nr = r+dr[i]
    #         nc = c+dc[i]
    #         print(nr, nc)
    #         if visit[nr][nc]:
    #             cnt  += 1
    #             break
    #         if nr == 0 and nr == N-1 and nc == 0 and nc == N-1:
    #             break
    #         if maze[nr][nc]:
    #             cnt += 1
    #             break
    #         cnt = 0
    #         if maze[nr][nc]==3:
    #             arrive = 1
    #         visit[nr][nc] = 1
    # print(arrive)



