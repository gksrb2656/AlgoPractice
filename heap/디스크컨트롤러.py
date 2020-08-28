# import heapq
# def solution(jobs):
#     last = -1
#     now = 0
#     answer = 0
#     wait = []
#     n = len(jobs)
#     count = 0
#     while count<n:
#         for job in jobs:
#             if last<job[0]<=now:
#                 answer +=now-job[0]
#                 heapq.heappush(wait,job[1])
#         if wait:
#             answer += len(wait)*wait[0]
#             last = now
#             now+=heapq.heappop(wait)
#             count += 1
#         else:
#             now += 1
#     return answer//n

import heapq
from collections import deque

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda y: (y[1], y[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
    return total_response_time // len(jobs)

solution([[3,0],[1,9],[2,6]])