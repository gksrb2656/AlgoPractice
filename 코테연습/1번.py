def solution(N, simulation_data):
    answer = 0
    info = []
    for s in simulation_data:
        if len(info) == N:
            if min(info) >= s[0]:
                answer += min(info) - s[0]
                info[info.index(min(info))] += s[1]
            else:
                info[info.index(min(info))] += s[0] - min(info) + s[1]

        else:
            info.append(s[0]+s[1])
    return answer

solution(2, [[0,3], [2,5], [4,2], [5,3]])