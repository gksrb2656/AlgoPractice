def summ(v, N, nums):
    if v == N:
        return sums.append(nums)
    for i in range(N):
        if i not in visit:
            if sums:
                if min(sums) < nums:
                    return
            nums += arr[v][i]
            visit.append(i)
            summ(v + 1, N, nums)
            nums -= arr[v][i]
            visit.pop()


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sums = []
    visit = []
    summ(0,N,0)
    print("#{} {}".format(t, min(sums)))