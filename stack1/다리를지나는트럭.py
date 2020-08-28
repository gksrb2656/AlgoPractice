from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    count = 0
    num = len(truck_weights)
    t = deque()
    w = deque()
    truck_weights = deque(truck_weights)
    while count != num:
        answer += 1
        if truck_weights and sum(w)+truck_weights[0]<=weight:
            w.append(truck_weights.popleft())
            for i in range(len(t)):
                t[i] += 1
            t.append(1)
        else:
            for i in range(len(t)):
                t[i] += 1
        if t[0]>=bridge_length:
            count += 1
            w.popleft()
            t.popleft()
    return print(answer+1)

solution(2, 10, [7, 4, 5, 6])
