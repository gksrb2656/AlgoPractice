from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def DFS(r,c,k):
    global Max
    for d in range(4):
        nr,nc = r+dr[d], c+dc[d]
        if nr>R-1 or nc>C-1 or nr<0 or nc<0:continue
        if visit[arr[nr][nc]]:continue
        visit[arr[nr][nc]] = 1
        DFS(nr,nc,k+1)
        visit[arr[nr][nc]] = 0
    if Max<k:
        Max = k
    if Max == 26:
        return

R, C = map(int,input().split())
arr = [list(map(ord,list(input()))) for _ in range(R)]
visit = [0]*91
visit[arr[0][0]] = 1
Max = 0
DFS(0,0,1)
print(Max)