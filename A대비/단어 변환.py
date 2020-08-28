from collections import deque
def solution(begin, target, words):
    if target in words:
        pass
    else:
        return 0
    check = [0]*len(words)
    Q = deque()
    Q.append((begin,0))
    while Q:
        w, time = Q.popleft()
        if w == target:
            return time
        for i in range(len(words)):
            if check[i]:continue
            cnt = 0
            for s in range(len(target)):
                if w[s] == words[i][s]:
                    cnt += 1
            if cnt == len(target)-1:
                check[i] = 1
                Q.append((words[i],time+1))

solution(	"hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])