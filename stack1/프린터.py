from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    num = len(priorities)
    que = deque([i for i in range(num)])
    answer = 0
    sheet = 0
    while 1:
        flag = 0
        page = priorities.popleft()
        for p in priorities:
            if p>page:
                flag = 1
                priorities.append(page)
                que.append(que.popleft())
                break
        if not flag:
            answer += 1
            if que[0] == location:
                return answer
            que.popleft()

solution([2, 1, 3, 2], 2)