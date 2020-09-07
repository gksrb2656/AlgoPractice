# def solution(n, build_frame):
#     answer = []
#     arr = [[[0, 0] for _ in range(n+1)] for _ in range(n)]
#     arr = [[[1, 0] for _ in range(n+1)]] + arr
#     for y, x, a, b in build_frame:
#         if a == 0:
#             if b:
#                 if arr[x][y][0] or arr[x][y][1]:
#                     arr[x][y][0] += 1
#                     arr[x + 1][y][0] += 1
#                     answer.append([y,x,0])
#             else:
#                 if arr[x + 1][y][0] == 1:
#                     if arr[x + 1][y][1] == 0:
#                         arr[x + 1][y][0] -= 1
#                         arr[x][y][0] -= 1
#                         answer.remove([y,x,0])
#                     elif arr[x + 1][y][1] == 1:
#                         if arr[x + 1][y + 1][1]:
#                             if arr[x + 1][y + 1][0]:
#                                 arr[x + 1][y][0] -= 1
#                                 arr[x][y][0] -= 1
#                                 answer.remove([y, x, 0])
#                         elif y > 0 and arr[x + 1][y - 1][1] == 1:
#                             if arr[x + 1][y - 1][0]:
#                                 arr[x + 1][y][0] -= 1
#                                 arr[x][y][0] -= 1
#                                 answer.remove([y, x, 0])
#                     elif arr[x + 1][y][1] == 2:
#                         arr[x + 1][y][0] -= 1
#                         arr[x][y][0] -= 1
#                         answer.remove([y,x,0])
#
#         else:
#             if b:
#                 if arr[x][y][0] or arr[x][y+1][0]:
#                     arr[x][y][1] += 1
#                     arr[x][y+1][1] += 1
#                     answer.append([y,x,1])
#                 elif arr[x][y][1] and arr[x][y+1][1]:
#                     arr[x][y][1] += 1
#                     arr[x][y+1][1] += 1
#                     answer.append([y,x,1])
#
#             else:
#                 if arr[x][y][0]:
#                     if arr[x][y+1][1] == 1:
#                         arr[x][y][1] -= 1
#                         arr[x][y+1][1] -= 1
#                         answer.remove([y, x, 1])
#                     elif arr[x][y+1] == 2:
#                         if arr[x][y+2][0]:
#                             arr[x][y][1] -= 1
#                             arr[x][y + 1][1] -= 1
#                             answer.remove([y, x, 1])
#                 elif arr[x][y][1] == 2:
#                     if not arr[x][y+1][0]:
#                         if y and arr[x][y+2][0] and arr[x][y-1][0]:
#                             arr[x][y][1] -= 1
#                             arr[x][y+1][1] -= 1
#                             answer.remove([y, x, 1])
#     for ar in arr:
#         print(ar)
#     print()
#     answer = sorted(answer, key = lambda x:(x[0], x[1], x[2]))
#     print(answer)
#     return answer
#
# solution(	5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]])
#실패한 내 코드..

def check(answer):
    for a in answer:
        y, x, k = a
        if k==0:
            if x==0 or [y, x-1, 0] in answer or [y-1,x,1] in answer or [y,x,1] in answer:
                continue
            else:
                return 0
        elif k==1:
            if [y,x-1,0] in answer or [y+1,x-1,0] in answer or ([y-1,x,1] in answer and [y+1,x,1] in answer):
                continue
            else:
                return 0
    return 1

def solution(n, buildframe):
    answer = []
    for y, x, a, b in buildframe:
        if b:
            answer.append([y,x,a])
            if check(answer):
                continue
            else:
                answer.remove([y,x,a])
        else:
            if [y,x,a] in answer:
                answer.remove([y,x,a])
            if check(answer):
                continue
            else:
                answer.append([y,x,a])
    answer.sort()
    return answer
solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]])

# 다른 사람 풀이 읽자.