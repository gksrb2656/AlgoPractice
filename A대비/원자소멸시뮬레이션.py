# from collections import deque
# dir = {0:(1,0), 1:(-1,0), 2:(0,-1), 3:(0,1)}
# def BFS():
#     global ans
#     while Q:
#         global ans
#         x,y,d,k,depth = Q.popleft()
#         if arr[y][x][0]:
#             continue
#         if arr[y][x][0] != k:
#             ans += arr[y][x][0]
#             arr[y][x] = [0, 0]
#             continue
#         arr[y][x] = [0,0]
#         ny = y+dir[d][0]
#         nx = x+dir[d][1]
#         if -2000<=nx<=2000 and -2000<=ny<=2000:
#             if arr[ny][nx][0]:
#                 if arr[ny][nx][1] == depth+1:
#                     arr[ny][nx][0] += k
#                     Q.append((nx,ny,d,k,depth+1))
#                 else:
#                     arr[ny][nx][0] = k
#                     Q.append((nx, ny, d, k, depth + 1))
#             else:
#                 arr[ny][nx][0] = k
#                 arr[ny][nx][1] = depth+1
#                 Q.append((nx,ny,d,k,depth+1))
#
# for t in range(1, int(input())+1):
#     N = int(input())
#     Q = deque()
#     ans = 0
#     arr = [[[0,0] for _ in range(4001)] for _ in range(4001)]
#     for _ in range(4):
#         x, y, d, k = map(int, input().split())
#         x, y = 2*(x+1000), 2*(y+1000)
#         arr[y][x][0] = k
#         Q.append((x,y,d,k,0))
#     print(Q)
#     BFS()
#     print(ans)
#     del arr
#
# from collections import deque
#
# dir = {0:(1,0), 1:(-1,0), 2:(0,-1), 3:(0,1)}
# for t in range(1, int(input())+1):
#     N = int(input())
#     Q = deque()
#     ans = 0
#     for _ in range(N):
#         x, y, d, k = map(int, input().split())
#         Q.append((2*x,2*y,d,k))
#     for i in range(4000):
#         pos = dict()
#         directions = dict()
#         for j in range(len(Q)):
#             x, y, d, k = Q.popleft()
#             ny = y+dir[d][0]
#             nx = x+dir[d][1]
#             if -2000 <= nx <= 2000 and -2000 <= ny <= 2000:
#                 if pos.get((nx,ny)):
#                     pos[(nx,ny)].append(k)
#                 else:
#                     pos[(nx,ny)] = [k]
#                     directions[(nx,ny)] = d
#         for key, value in pos.items():
#             if len(value)>1:
#                 ans += sum(value)
#             else:
#                 x, y = key
#                 k = value[0]
#                 d = directions[key]
#                 Q.append((x,y,d,k))
#     print("#{} {}".format(t,ans))




for t in range(1,int(input())+1):
    N = int(input())
    arr = []
    for _ in range(N):
        x, y, d, k = map(int, input().split())
        x, y = 2*x, 2*y
        arr.append([x,y,d,k])
    ans = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i][0] == arr[j][0]:
                if arr[i][2]+arr[i][2] == 5:
                    ans += arr[i][3]+arr[j][3]
            elif arr[i][1] == arr[j][1]:
                if arr[i][2] + arr[i][2] == 1:
                    ans += arr[i][3] + arr[j][3]
            elif abs(arr[i][0]-arr[j][0]) == abs(arr[i][1]-arr[j][1]):
                if arr[]