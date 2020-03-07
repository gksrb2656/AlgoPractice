# from copy import deepcopy
#
# def DFS(k,people_n):
#     global Min
#     if k == people_n:
#         Max = cal()
#         Min = min(Min,Max)
#         return
#
#     for s in range(2):
#         dis = abs(people[k][0]-stare[s][0])+abs(people[k][1]-stare[s][1])
#         s_copy = deepcopy(select_stare[s])
#         select_stare[s].append(dis+stare[s][2])
#         DFS(k+1,people_n)
#         select_stare[s] = s_copy
#
#
# def cal():
#     Max = 0
#     for i in range(2):
#         select_stare[i].sort()
#         if len(select_stare[i])>3:
#             for j in range(3,len(select_stare[i])):
#                 if select_stare[i][j]-stare[i][2]<select_stare[i][j-3]:
#                     select_stare[i][j] = select_stare[i][j-3] + stare[i][2]
#         if select_stare[i]:
#             Max = max(select_stare[i][-1],Max)
#     return Max
#
# T = int(input())
# for t in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     people = []
#     stare = []
#     Min = 200
#     people_n = 0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 1:
#                 people.append((i,j))
#                 people_n += 1
#             elif arr[i][j]:
#                 stare.append((i,j,arr[i][j]))
#     select_stare = [[] for _ in range(2)]
#     DFS(0,people_n)
#     print("#{} {}".format(t,Min+1))

##----좋은 답안----##
def calc_time(comb, group):
    if len(comb) == 0:
        return 0
    comb.sort()
    if len(comb) > 3:
        for j in range(3, len(comb)):
            comb[j] = max(comb[j], comb[j - 3] + stairs_len[group])
    return comb[-1] + 1 + stairs_len[group]


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    man = []
    stair = []
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                man.append((r, c))
            elif board[r][c]:
                stair.append((r, c))
    n_man = len(man)
    stairs_len = [board[stair[i][0]][stair[i][1]] for i in range(2)]

    time_to_stair = [[abs(i[0] - stair[j][0]) + abs(i[1] - stair[j][1])
                      for j in range(2)] for i in man]

    min_time_consumed = 2147000000
    for i in range(0, 1 << n_man):
        comb1 = []
        comb2 = []
        for j in range(n_man):
            if i & (1 << j):
                comb1.append(time_to_stair[j][0])
            else:
                comb2.append(time_to_stair[j][1])
        comb1_time = calc_time(comb1, 0)
        comb2_time = calc_time(comb2, 1)
        time_consumed = max(comb1_time, comb2_time)

        min_time_consumed = min(min_time_consumed, time_consumed)

    print("#{} {}".format(t, min_time_consumed))