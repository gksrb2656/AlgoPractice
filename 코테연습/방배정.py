def solution(k, room_number):
    memo = dict()
    answer = [0]*len(room_number)
    cnt = 0
    for i in room_number:
        flag = 0
        v = i
        nodes = [v]
        while not flag:
            if not memo.get(v):
                flag = 1
                answer[cnt] = v
                memo[v] = v+1
                for n in nodes:
                    memo[n] = v+1
                break
            else:
                nodes +=[memo[v]]
                v = memo[v]
        cnt += 1
    return answer