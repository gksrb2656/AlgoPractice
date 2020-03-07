# from collections import deque
# def Queen(N):
#     Q = deque()
#     cnt = 0
#     for j in range(N):
#         Q.append((0, j))
#         visit = [(0,j)]
#         for r in range(N):
#                     visit.append((r, c))
#         if len(visit) == N:
#             cnt += 1
#     return cnt
def Queen(s_p):
    r = s_p + 1
    for j in range(N):
        if

T = int(input())
for t in range(1, T+1):
    N = int(input())
    case = Queen(N)
    print("#{} {}".format(t, case))
