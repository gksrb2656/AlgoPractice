# from collections import deque
#
# def DFS(depth,s):
#     flag = 0
#     global p_25, ans
#     if depth == 10:
#         ans = max(s,ans)
#         return
#
#     for i in range(1,5):
#         if charic[i][0][charic[i][1]] == 'end':
#             continue
#         elif charic[i][0] in (no_b, b_25) and charic[i][1]+dice[depth]>=len(charic[i][0])-1:
#             temp = charic[i][1]
#             charic[i][1] = len(charic[i][0])-1
#             DFS(depth+1,s)
#             charic[i][1] = temp
#             continue
#         if charic[i][1]+dice[depth]<len(charic[i][0]) and charic[i][0][charic[i][1]+dice[depth]]==25:
#             if p_25:continue
#         if charic[i][0]==no_b and charic[i][0][charic[i][1]+dice[depth]] == 10:
#             charic[i][0] = b_10
#             temp = charic[i][1]
#             charic[i][1] = 0
#             for j in range(1,5):
#                 if i==j:continue
#                 if [charic[i][0], charic[i][1]] in [charic[j][0], charic[j][1]]:
#                     charic[i][0] = no_b
#                     charic[i][1] = temp
#                     flag = 1
#                     break
#             if flag:continue
#             DFS(depth+1,s + charic[i][0][charic[i][1]])
#             charic[i][0] = no_b
#             charic[i][1] = temp
#         elif charic[i][0]==no_b and charic[i][0][charic[i][1] + dice[depth]] == 20:
#             charic[i][0] = b_20
#             temp = charic[i][1]
#             charic[i][1] = 0
#             for j in range(1,5):
#                 if i==j:continue
#                 if [charic[i][0], charic[i][1]] in [charic[j][0], charic[j][1]]:
#                     charic[i][0] = no_b
#                     charic[i][1] = temp
#                     flag = 1
#                     break
#             if flag:continue
#             DFS(depth+1,s + charic[i][0][charic[i][1]])
#             charic[i][0] = no_b
#             charic[i][1] = temp
#         elif  charic[i][0]==no_b and charic[i][0][charic[i][1] + dice[depth]] == 30:
#             charic[i][0] = b_30
#             temp = charic[i][1]
#             charic[i][1] = 0
#             for j in range(1,5):
#                 if i==j:continue
#                 if [charic[i][0], charic[i][1]] in [charic[j][0], charic[j][1]]:
#                     charic[i][0] = no_b
#                     charic[i][1] = temp
#                     flag = 1
#                     break
#             if flag:continue
#             DFS(depth+1,s + charic[i][0][charic[i][1]])
#             charic[i][0] = no_b
#             charic[i][1] = temp
#         elif charic[i][1]+dice[depth]>=len(charic[i][0])-1:
#             temp = charic[i][1]
#             temp_node = charic[i][0]
#             charic[i][1] = charic[i][1]+dice[depth]-len(temp_node)
#             charic[i][0] = b_25
#             if [charic[i][0], charic[i][1]] in charic.values():
#                 charic[i][0] = no_b
#                 charic[i][1] = temp
#                 continue
#             DFS(depth+1, s+charic[i][0][charic[i][1]])
#             charic[i][0] = temp_node
#             charic[i][1] = temp
#         else:
#             if charic[i][0][charic[i][1]] == 25:
#                 p_25 = False
#             charic[i][1] += dice[depth]
#             if charic[i][0][charic[i][1]] == 25:
#                 p_25 = True
#             DFS(depth+1,s + charic[i][0][charic[i][1]])
#             charic[i][1] -= dice[depth]
#             if charic[i][0][charic[i][1]] == 25:
#                 p_25 = True
#
# dice = list(map(int, input().split()))
# no_b = [i for i in range(0,41,2)]+[0]
# b_10 = [10,13,16,19,25]
# b_20 = [20,22,24,25]
# b_25 = [25,30,35,40,0]
# b_30 = [30,28,27,26,25]
# p_25 = False
# charic = {1:[no_b,0],2:[no_b,0],3:[no_b,0],4:[no_b,0]}
# ans = 0
# DFS(0,0)
# print(ans)
#
# def DFS(depth,s):
#     global ans
#     if depth == 10:
#         ans = max(s,ans)
#         return
#
#     for i in range(1,5):
#



dice = list(map(int, input().split()))
board = [[i for i in range(0,41,2)]+[0],
        [13,16,19],
        [22,24],
        [25,30,35],
        [28,27,26]]

visit = [[0]*22,[0]*3,[0]*2,[0]*3,[0]*3]
charic = [[0,0]*4] # index, node
ans = 0