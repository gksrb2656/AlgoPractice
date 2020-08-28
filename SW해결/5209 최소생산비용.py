# def DFS(depth,s):
#     global ans, MAX, cnt
#     cnt += 1
#     if depth == N+1:
#         ans = min(ans,s)
#         return
#
#     for i in range(N):
#         if visit[i]:continue
#         visit[i] = 1
#         DFS(depth+1,s+items[depth][i])
#         visit[i] = 0
#
#
# for t in range(1,int(input())+1):
#     N = int(input())
#     items = dict()
#     visit = [0]*N
#     ans = 100*N
#     MIN = 100
#     cnt = 0
#     for i in range(1,N+1):
#         items[i] = list(map(int, input().split()))
#         sMIN = min(items[i])
#         MIN = min(MIN,sMIN)
#     DFS(1,0)
#     print("#{} {}".format(t,ans))
#     print(cnt)
#
def DFS(depth,s):
    global memo,cnt
    if depth == N:
        memo=s
        return

    if s+((N-depth)*MIN)>=memo:
        return

    for i in range(N):
        flag = 0
        if visit[i]:continue
        if memo<s+arr[depth][i]:
            flag = 1
        if flag:continue
        visit[i] = 1
        DFS(depth+1,s+arr[depth][i])
        visit[i] = 0

for t in range(1,int(input())+1):
    N = int(input())
    visit= [0]*N
    cnt = 0
    MIN = 100
    arr = [list(map(int,input().split())) for _ in range(N)]
    for i in arr:
        for j in i:
            MIN = min(MIN, j)
    memo = 100*N
    DFS(0,0)
    print("#{} {}".format(t,memo))
    print(cnt)
# #
#
# def DFS(depth,s,idx):
#     global ans, cnt
#     cnt += 1
#     if depth>=N:
#         if dp[depth-1][idx]> s:
#             dp[depth - 1][idx] = s
#             ans = min(ans,s)
#         return
#     for i in range(N):
#         flag = 0
#         if visit[i]:continue
#         if dp[depth][i]<s+arr[depth][i] or ans<s+arr[depth][i]:
#             continue
#         visit[i] = 1
#         DFS(depth+1,s+arr[depth][i],i)
#         dp[depth-1][idx] = min(dp[depth][i],dp[depth-1][idx])
#         visit[i] = 0
#
# for t in range(1,int(input())+1):
#     N = int(input())
#     visit= [0]*N
#     cnt = 0
#     ans = 99999
#     arr = [list(map(int,input().split())) for _ in range(N)]
#     dp = [[99999]*N for _ in range(N)]
#     DFS(0,0,0)
#     print("#{} {}".format(t,ans))
#     print(cnt)
# #
# for t in range(1,int(input())+1):
#     N = int(input())
#     visit= [0]*N
#     ans = 99999
#     arr = [list(map(int,input().split())) for _ in range(N)]
#     dp = [[99999]*N for _ in range(N)]
#     print("#{} {}".format(t,ans))

#
#
# # 1
# # 10
# # 1 2 3 4 5 6 7 8 9 10
# # 1 2 3 4 5 6 7 8 9 10
# # 1 2 3 4 5 6 7 8 9 10
# # 1 2 3 4 5 6 7 8 9 10
# # 1 2 3 4 5 6 7 8 9 10
# # 1 2 3 4 5 6 7 8 9 10
# # 1 2 3 4 5 6 7 8 9 10
# # 1 2 3 4 5 6 7 8 9 10
# # 1 2 3 4 5 6 7 8 9 10
# # 1 2 3 4 5 6 7 8 9 10
#
# # 1
# # 15
# # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15