def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)

    r = distance
    l = 0
    while l <= r:
        last = 0
        cnt = 0
        flag = 0
        mid = (r + l) // 2
        for i in range(len(rocks)):
            if rocks[i]-last < mid:
                cnt += 1
                if cnt > n:
                    flag = 1
                    break
            else:
                last = rocks[i]
        if flag:
            r = mid - 1
        else:
            l = mid + 1
            answer = mid
    return answer

solution(25, [2, 14, 11, 21, 17], 2)