def solution(clothes):
    answer = 1
    has = {}
    for cloth, category in clothes:
        if category in has:
            has[category] += 1
        else:
            has[category] = 1

    for c in has.values():
        answer *= (c+1)
    return answer-1

solution([['yellow_hat', 'face'], ['blue_sunglasses', 'face'], ['green_turban', 'face']])