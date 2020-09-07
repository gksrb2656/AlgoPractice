# def solution(n, weak, dist):
#     answer = 0
#     intervals = []
#     for i in range(len(weak)-1):
#         intervals.append([weak[i+1]-weak[i],i,i+1])
#     intervals.append([(n+weak[0]-weak[-1]),0,len(weak)-1])
#     intervals.sort(reverse=True)
#     check = [0]*len(weak)
#     dist.sort(reverse=True)
#     for i in range(1,len(dist)+1):
#         if i == len(weak):
#             return i
#         n -= intervals[i-1][0]
#         check[intervals[i-1][1]] += 1
#         if check[intervals[i-1][1]] == 2:
#             dist = dist[:-1]
#         check[intervals[i-1][2]] += 1
#         if check[intervals[i-1][2]] == 2:
#             dist = dist[:-1]
#         if n<=sum(dist[:i]):
#             return i
#     return -1
# print(solution(	200, [1,50,100,150,200], [1, 2, 3, 4]))
# 후... 실패

from itertools import permutations
def check(n,dist,weak):
    for st in range(len(weak)):
        weak_rotate = weak[st:] +weak[:st]
        for dist_p in permutations(dist):
            weak_copy = weak_rotate[:]
            cnt = 0
            for d in dist_p:
                cnt += 1
                while d>=0:
                    if cnt == len(weak):
                        return 1
                    if weak_copy[1]<weak_copy[0]:
                        interval = weak_copy[1]+n-weak_copy[0]
                    else:
                        interval = weak_copy[1]-weak_copy[0]
                    if interval<=d:
                        d -= interval
                        weak_copy = weak_copy[1:]+weak_copy[:1]
                        cnt += 1
                        if cnt == len(weak):
                            return 1
                    else:
                        weak_copy = weak_copy[1:] + weak_copy[:1]
                        break
    return 0


def solution(n, weak, dist):
    answer = 0
    dist.sort(reverse=True)
    for i in range(1,len(dist)+1):
        if check(n,dist[:i],weak):
            return i
    return -1

print(solution(	12, [1, 5, 6, 10], [1, 2, 3, 4]))