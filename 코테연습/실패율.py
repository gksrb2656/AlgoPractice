# from collections import defaultdict
def solution(N, stages):
    answer = []
    fail_ratio =[0]*(N+2)
    for stage in stages:
        fail_ratio[stage] += 1
    for stage in range(1,N+1):
        fail_ratio[stage] = [stage,fail_ratio[stage]/(sum(fail_ratio[stage+1:])+fail_ratio[stage]) if (sum(fail_ratio[stage+1:])+fail_ratio[stage]) else 1]
    fail_ratio= fail_ratio[1:N+1]
    fail_ratio.sort(key=lambda x:x[1] if x else 1,reverse=True)
    answer = [data[0] for data in fail_ratio]
    return answer

solution(5,[2, 1, 2, 6, 2, 4, 3, 3])
