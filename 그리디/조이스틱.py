def solution(name):
    answer = 0
    idx = []
    for i in range(len(name)):
        if name[i] != 'A':
            idx.append(i)
    now = 0
    last = 0
    point = 0
    while idx:
        Min = 26
        for i in range(len(idx)):
            if Min>min(abs(idx[i]-now), abs(len(name)-idx[i]+now)):
                Min = min(abs(idx[i]-now), abs(len(name)-idx[i]+now))
                point = i
        last = now
        now = idx[point]
        idx.pop(point)
        answer += min(abs(ord(name[now]) - ord('A')),abs(-ord(name[now]) + ord('Z')+1))
        answer += Min
    return print(answer)

solution("BBAABB")
