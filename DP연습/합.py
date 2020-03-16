T = int(input())
for t in range(1,T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    n = 0
    S = nums[0]
    Max = S
    for i in range(1,N):
        if S+nums[i]<0 or S<0:
            S = nums[i]
        else:
            S += nums[i]
        if S>Max:
            Max = S
    print("#{} {}".format(t,Max))