def solution(road, n):
    roads = list(map(int, road))
    crack = []
    n_crack = roads.count(0)
    original_cnt = 0
    cnt = 0
    if n >= n_crack:
        return len(road)

    for i in range(len(roads)):
        if roads[i]:
            cnt += 1
        else:
            cnt = 0
            original_cnt = max(original_cnt, cnt)
            crack.append(i)
    if cnt:
        original_cnt = max(original_cnt, cnt)
    if n == 0:
        return original_cnt

    max_roads = 0
    for m in range(n_crack - n):
        cnt = 0
        for i in crack[m:m + n]:
            roads[i] = 1
        if m:
            st = 0
        else:
            st = crack[m - 1]
        for i in range(st, len(roads)):
            if roads[i]:
                cnt += 1
            else:
                max_roads = max(cnt, max_roads)
                cnt = 0
        if cnt:
            max_roads = max(cnt, max_roads)
        for i in crack[m:m + n]:
            roads[i] = 0

    return max_roads

solution("111011110011111011111100011111", 3)