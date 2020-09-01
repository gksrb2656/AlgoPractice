from collections import deque


def solution(T, R, K):
    def bfs(v):
        nonlocal answer
        Q = deque()
        Q.append((K,T[K-1]))
        while Q:
            v,time = Q.popleft()
            answer = max(time, answer)
            for i in range(len(R)):
                if R[i][1] == v:
                    Q.append((R[i][0],T[R[i][0]]+time))
    answer = 0
    bfs(K)
    return answer

print(solution([5,8,3,7,10,5,4],[[1,2],[2,4],[1,4],[6,5],[3,5],[4,6]],5))