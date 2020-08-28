def solution(n, times):
    l = 1
    r = max(times)*n
    answer = 0
    while l <= r:
        mid = (l + r) // 2
        flag = 0
        people = 0
        for t in times:
            people += mid // t
            if people >= n:
                flag = 1
                answer = mid
                break
        if flag:
            r = mid - 1
        else:
            l = mid + 1
    return answer

solution(6, [7, 10])