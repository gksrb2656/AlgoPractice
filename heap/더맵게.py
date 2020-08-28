# import heapq
# def solution(scoville, K):
#     answer = 0
#     heapq.heapify(scoville)
#     while scoville[0]<K:
#         answer += 1
#         if not scoville:
#             return -1
#         Min = heapq.heappop(scoville)
#         if not scoville:
#             return -1
#         Min2 = heapq.heappop(scoville)
#         heapq.heappush(scoville,Min+2*Min2)
#     return answer

from collections import deque
def solution(scoville, K):
    answer = 0
    que = deque()
    scoville = deque(scoville)
    while scoville:
        Mins = []
        while len(Mins)<2 and scoville:
            while que and que[0]<=scoville[0]:
                Mins.append(que.popleft())
            if len(Mins)<2:
                Mins.append(scoville.popleft())
        if len(Mins) == 2:
            que.append(Mins[0]+Mins[1]*2)
        answer += 1
        if scoville:
            if scoville[0]>K:
                if que[0]>K:
                    return answer
                else:
                    return answer+1
    return -1

solution([1, 2, 3, 9, 10, 12], 12)