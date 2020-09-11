from collections import defaultdict

def solution(food_times, k):
    answer = 0
    f_copy = list(set(food_times))
    f_copy.sort()
    m_idx = 0
    len_f=len_f2 = len(food_times)
    times_num = defaultdict(int)

    for f in range(len_f):
        times_num[food_times[f]] += 1

    interval = f_copy[m_idx]
    while k >= len_f * interval:
        k -= len_f * interval
        len_f -= times_num[f_copy[m_idx]]
        if len_f <= 0:
            return -1
        interval = f_copy[m_idx + 1] - f_copy[m_idx]
        m_idx += 1
    if k>=len_f:
        k %= len_f
    cnt = 0
    for t in range(len_f2):
        if food_times[t]>=f_copy[m_idx]:
            if k == cnt:
                return t+1
            else:
                cnt += 1