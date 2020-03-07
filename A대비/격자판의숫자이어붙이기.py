# from collections import deque

# dr = [1,-1,0,0]
# dc = [0,0,1,-1]
#
# def DFS(k,i,j,nums):
#     global cnt
#     if k == 6:
#         if nums in num_set:return
#         num_set.append(nums)
#         cnt += 1
#         return
#     for d in range(4):
#         nr = i + dr[d]
#         nc = j + dc[d]
#         if nr>3 or nc>3 or nr<0 or nc<0:continue
#         DFS(k+1,nr,nc,nums+arr[nr][nc])
#
# T = int(input())
# for t in range(1,T+1):
#     arr = [list(input().split()) for _ in range(4)]
#     num_set = []
#     cnt = 0
#     for i in range(4):
#         for j in range(4):
#             DFS(0,i,j,arr[i][j])
#     print(cnt)

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def DFS(k,i,j,nums):
    global cnt
    if k == 6:
        num_set.add(nums)
        return
    for d in range(4):
        nr = i + dr[d]
        nc = j + dc[d]
        if nr>3 or nc>3 or nr<0 or nc<0:continue
        DFS(k+1,nr,nc,nums+arr[nr][nc])

T = int(input())
for t in range(1,T+1):
    arr = [list(input().split()) for _ in range(4)]
    num_set = set()
    cnt = 0
    for i in range(4):
        for j in range(4):
            DFS(0,i,j,arr[i][j])
    print(len(num_set))