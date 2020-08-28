# from collections import deque
#
# def solution(progresses, speeds):
#     answer = []
#     progresses = deque(progresses)
#     speeds = deque(speeds)
#     stack = []
#     while progresses:
#         p = progresses.popleft()
#         s = speeds.popleft()
#         days = (100-p)//s
#         if (100-p)%s:
#             days += 1
#         if not stack:
#             stack.append(days)
#             answer.append(1)
#         elif stack[-1]>=days:
#             answer[-1] += 1
#         else:
#             answer.append(1)
#     return print(answer)

def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

solution([99,96,97],[1,3,7])