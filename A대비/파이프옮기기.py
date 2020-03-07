# def DFS(i, j, dir):
#     global cnt
#     if i == j == N - 1:
#         cnt += 1
#         return
#
#     if dir == 0:
#         if i+1<= N-1 and arr[i+1][j] == 0:
#             DFS(i+1,j,0)
#         if i+1<= N-1 and j+1<=N-1 and arr[i + 1][j]==0 and arr[i][j + 1]==0 and arr[i + 1][j + 1]==0:
#             DFS(i+1,j+1,2)
#     elif dir == 1:
#         if j+1<= N-1 and arr[i][j+1] == 0:
#             DFS(i,j+1,1)
#         if i+1<= N-1 and j+1<=N-1 and arr[i + 1][j]==0 and arr[i][j + 1]==0 and arr[i + 1][j + 1]==0:
#             DFS(i+1,j+1,2)
#     elif dir == 2:
#         if j+1<= N-1 and arr[i][j+1] == 0:
#             DFS(i,j+1,1)
#         if i+1<= N-1 and j+1<=N-1 and arr[i + 1][j]==0 and arr[i][j + 1]==0 and arr[i + 1][j + 1]==0:
#             DFS(i+1,j+1,2)
#         if i+1<= N-1 and arr[i+1][j] == 0:
#             DFS(i+1,j,0)
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# cnt = 0
# DFS(0, 1, 1)
# print(cnt)

N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
result = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
result[0][1][0] = 1
for i in range(N):
    for j in range(2, N):
        if data[i][j] == 0:
            result[i][j][0] = result[i][j - 1][0] + result[i][j - 1][2]
            if i > 0:
                result[i][j][1] = result[i - 1][j][1] + result[i - 1][j][2]
                if data[i - 1][j] == 0 and data[i][j - 1] == 0:
                    result[i][j][2] = result[i - 1][j - 1][0] + result[i - 1][j - 1][1] + result[i - 1][j - 1][2]
        for jj in result:
            print(jj)
        print()
print(sum(result[N - 1][N - 1]))