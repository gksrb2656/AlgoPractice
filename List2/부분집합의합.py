def get_power_set(s):
    power_set = [[]]
    for elem in s:
        # iterate over the sub sets so far
        for sub_set in power_set:
            # add a new subset consisting of the subset at hand added elem
            power_set = power_set + [list(sub_set) + [elem]]
            print(power_set)
    return power_set

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    li = [i for i in range(1, 13)]
    li = get_power_set(li)
    cnt = 0
    for i in li:
        if sum(i) == K:
            cnt += 1
    print("#{0} {1}".format(t, cnt))


