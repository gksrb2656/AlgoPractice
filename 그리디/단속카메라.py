def solution(routes):
    answer = 0
    routes.sort()

    standard = routes[0][1]
    routes.pop(0)
    answer+=1

    for item in routes:
        if item[0] <= standard:
            standard = min(item[1],standard)
        else:
            standard = item[1]
            answer+=1
    return answer
print(solution([[-20, -15], [-10, -5], [-15, -10], [-5, -3]]))