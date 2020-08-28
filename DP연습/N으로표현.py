# def solution(N, number):
#     S = [0, {N}]
#     for i in range(2, 9):
#         case_set = {int(str(N)*i)}
#         for i_half in range(1, i//2+1):  # S[i_half] S[1]
#             for x in S[i_half]:
#                 for y in S[i-i_half]:
#                     case_set.add(x+y)
#                     case_set.add(x-y)
#                     case_set.add(y-x) # y-x 케이스 추가
#                     case_set.add(x*y)
#                     if x != 0:
#                         case_set.add(y//x)
#                     if y != 0:
#                         case_set.add(x//y)
#         if number in case_set:
#             return i
#         S.append(case_set)
#     return -1

answer = -1

def DFS(n, pos, num, number, s):
    global answer
    if pos > 8:
        return
    if num == number:
        if pos < answer or answer == -1:
            #print(s)
            answer=pos
        return

    nn=0
    for i in range(8):
        nn=nn*10+n
        DFS(n, pos+1+i, num+nn, number, s+'+')
        DFS(n, pos+1+i, num-nn, number, s+'-')
        DFS(n, pos+1+i, num*nn, number, s+'*')
        DFS(n, pos+1+i, num/nn, number, s+'/')

def solution(N, number):
    DFS(N, 0, 0, number, '')
    return answer

solution(5,12)