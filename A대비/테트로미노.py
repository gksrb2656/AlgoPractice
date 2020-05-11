# def DFS(r,c,k,n_sum):
#     global MAX
#     global MAX_n
#     if n_sum+MAX_n*(3-k)<=MAX:
#         return
#     if k == 3:
#         if MAX<n_sum:
#             MAX = n_sum
#         return
#     for d in range(4):
#         nr = r+dr[d]
#         nc = c+dc[d]
#         if arr[nr][nc] == 0 or visit[nr][nc]:continue
#         if k == 1:
#             visit[nr][nc] = 1
#             n_sum += arr[nr][nc]
#             DFS(r,c,k+1,n_sum)
#             n_sum -= arr[nr][nc]
#             visit[nr][nc] = 0
#         visit[nr][nc] = 1
#         n_sum += arr[nr][nc]
#         DFS(nr,nc,k+1,n_sum)
#         n_sum -= arr[nr][nc]
#         visit[nr][nc] = 0
#
#
# dr = [-1,0,1,0]
# dc = [0,1,0,-1]
# N, M = map(int, input().split())
# arr = [[0]*(M+2)]
# for i in range(N):
#     arr.append([0]+list(map(int, input().split()))+[0])
# arr.append([0]*(M+2))
# visit = [[0]*(M+2) for _ in range(N+2)]
# MAX = 0
# MAX_n = 0
# for i in range(1,N+1):
#     for j in range(1,M+1):
#         if arr[i][j]>MAX_n:
#             MAX_n = arr[i][j]
#         visit[i][j] = 1
#         DFS(i,j,0,arr[i][j])
#         visit[i][j] = 0
# print(MAX)

def DFS(r,c,k,n_sum):
    global MAX
    global MAX_n
    if n_sum+MAX_n*(3-k)<=MAX:
        return
    if k == 3:
        if MAX<n_sum:
            MAX = n_sum
        return
    for d in range(4):
        nr = r+dr[d]
        nc = c+dc[d]
        if arr[nr][nc] == 0 or visit[nr][nc]:continue
        if k == 1:
            visit[nr][nc] = 1
            n_sum += arr[nr][nc]
            DFS(r,c,k+1,n_sum)
            n_sum -= arr[nr][nc]
            visit[nr][nc] = 0
        visit[nr][nc] = 1
        n_sum += arr[nr][nc]
        DFS(nr,nc,k+1,n_sum)
        n_sum -= arr[nr][nc]
        visit[nr][nc] = 0


dr = [-1,0,1,0]
dc = [0,1,0,-1]
N, M = map(int, input().split())
arr = [[0]*(M+2)]
for i in range(N):
    arr.append([0]+list(map(int, input().split()))+[0])
arr.append([0]*(M+2))
visit = [[0]*(M+2) for _ in range(N+2)]
MAX = 0
MAX_n = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        if arr[i][j]>MAX_n:
            MAX_n = arr[i][j]
for i in range(1,N+1):
    for j in range(1,M+1):
        visit[i][j] = 1
        DFS(i,j,0,arr[i][j])
        visit[i][j] = 0
print(MAX)