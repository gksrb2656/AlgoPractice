#
# dr = [1,-1,0,0]
# dc = [0,0,1,-1]
# def DFS(r,c):
#     global s
#     visit[r][c] = 1
#     for i in range(4):
#         nr = r+dr[i]
#         nc = c+dc[i]
#         if nr<0 or nc<0 or nr>N-1 or nc>N-1 or visit[nr][nc]:
#             continue
#         if arr[nr][nc] !='1':
#             continue
#         DFS(nr,nc)
#         s += 1
#
# N = int(input())
# arr = [list(input()) for _ in range(N)]
# cnt = 0
# visit = [[0]*N for _ in range(N)]
# house = []
# for i in range(N):
#     for j in range(N):
#         if not visit[i][j] and arr[i][j] == '1':
#             cnt += 1
#             s = 1
#             DFS(i,j)
#             house.append(s)
# print(cnt)
# house.sort()
# for i in house:
#     print(i)

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def dfs(r,c):
    global house
    house += 1
    complex[r][c] = '0'
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr>=0 and nr<N and nc>=0 and nc<N:
            if complex[nr][nc]=='1':
                dfs(nr,nc)

N = int(input())
complex = [list(input()) for _ in range(N)]
cnt = 0
ans = []
visit = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if complex[i][j]=='1':
            house = 0
            cnt += 1
            dfs(i,j)
            ans.append(house)

ans.sort()
print(cnt)
for jj in ans:
    print(jj)