dir = {0:(0,0), 1:(-1,0), 2:(0,1), 3:(1,0), 4:(0,-1)}
#
# T = int(input())
# for t in range(1,T+1):
#     arr = [[[0,0] for _ in range(11)] for _ in range(11)]
#     M,A = map(int, input().split())
#     A_move = list(map(int, input().split()))
#     B_move = list(map(int, input().split()))
#     for i in range(A):
#         c,r,rg,bt = map(int,input().split())
#         for row in range(1,11):
#             for col in range(1,11):
#                 if abs(row-r)+abs(col-c)<=rg:
#                     if arr[row][col][0]:
#                         if arr[row][col][0]<bt:
#                             arr[row][col][1] = arr[row][col][0]
#                             arr[row][col][0] = bt
#                         elif arr[row][col][1]<bt:
#                             arr[row][col][1] = bt
#                     else:
#                         arr[row][col][0]= bt
#     A_p = [1,1]
#     B_p = [10,10]
#     sum_bt = arr[0][0][0] + arr[10][10][0]
#     for m in range(M):
#         A_p[0] += dir[A_move[m]][0]
#         A_p[1] += dir[A_move[m]][1]
#         B_p[0] += dir[B_move[m]][0]
#         B_p[1] += dir[B_move[m]][1]
#         if arr[A_p[0]][A_p[1]][0] == arr[B_p[0]][B_p[1]][0]:
#             if arr[A_p[0]][A_p[1]][1] and arr[B_p[0]][B_p[1]][1]:
#                 sum_bt += max(sum(arr[A_p[0]][A_p[1]]),sum(arr[B_p[0]][B_p[1]]))
#             elif arr[A_p[0]][A_p[1]][1]:
#                 sum_bt+=sum(arr[A_p[0]][A_p[1]])
#             elif arr[B_p[0]][B_p[1]][1]:
#                 sum_bt+=sum(arr[B_p[0]][B_p[1]])
#             else:
#                 sum_bt += arr[B_p[0]][B_p[1]][0]
#
#         else:
#             sum_bt += arr[A_p[0]][A_p[1]][0]
#             sum_bt += arr[B_p[0]][B_p[1]][0]
#
#     print(sum_bt)

T = int(input())
for t in range(1,T+1):
    arr = [[[] for _ in range(11)] for _ in range(11)]
    M,A = map(int, input().split())
    A_move = list(map(int, input().split()))
    B_move = list(map(int, input().split()))
    APS = [[0]*4]
    for i in range(A):
        APS.append(list(map(int,input().split())))
    for i in range(1,A+1):
        c, r, rg, bt = APS[i]
        for row in range(1,11):
            for col in range(1,11):
                if abs(row-r)+abs(col-c)<=rg:
                    arr[row][col].append((bt,i))
                    arr[row][col].sort(reverse=True)

    A_p = [1,1]
    B_p = [10,10]
    sum_bt = 0
    if arr[1][1]:
        sum_bt += arr[1][1][0][0]
    if arr[10][10]:
        sum_bt += arr[10][10][0][0]
    for m in range(M):
        A_p[0] += dir[A_move[m]][0]
        A_p[1] += dir[A_move[m]][1]
        B_p[0] += dir[B_move[m]][0]
        B_p[1] += dir[B_move[m]][1]
        if arr[A_p[0]][A_p[1]] and arr[B_p[0]][B_p[1]]:
            if arr[A_p[0]][A_p[1]][0][1] == arr[B_p[0]][B_p[1]][0][1]:
                if len(arr[A_p[0]][A_p[1]])>1 and len(arr[B_p[0]][B_p[1]])>1:
                    sum_bt += max(arr[A_p[0]][A_p[1]][0][0]+arr[A_p[0]][A_p[1]][1][0],arr[A_p[0]][A_p[1]][0][0]+arr[B_p[0]][B_p[1]][1][0])
                elif len(arr[B_p[0]][B_p[1]])>1:
                    sum_bt += arr[B_p[0]][B_p[1]][0][0]+arr[B_p[0]][B_p[1]][1][0]
                elif len(arr[A_p[0]][A_p[1]])>1:
                    sum_bt += arr[B_p[0]][B_p[1]][0][0] + arr[A_p[0]][A_p[1]][1][0]
                else:
                    sum_bt += arr[A_p[0]][A_p[1]][0][0]
            else:
                sum_bt += arr[A_p[0]][A_p[1]][0][0]
                sum_bt += arr[B_p[0]][B_p[1]][0][0]
        else:
            if arr[A_p[0]][A_p[1]]:
                sum_bt += arr[A_p[0]][A_p[1]][0][0]
            if arr[B_p[0]][B_p[1]]:
                sum_bt += arr[B_p[0]][B_p[1]][0][0]

    print(sum_bt)