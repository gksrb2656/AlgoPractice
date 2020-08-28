from collections import deque

def solution(n, computers):
    answer = 0
    check = [0]*len(computers)
    Q = deque()
    for i in range(len(computers)):
        if check[i]:continue
        Q.append(i)
        check[i] = 1
        answer += 1
        while Q:
            v = Q.popleft()
            for j in range(len(computers)):
                if check[j] or j==v:continue
                if computers[v][j]:
                    Q.append(j)
                    check[j] = 1
                    break
    return answer
