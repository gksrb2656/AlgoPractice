# import sys
# sys.stdin = open("sample_input.txt", "r")
# T = int(input())
T = int(input())
for i in range(1,T+1):
    N = int(input())
    A = list(map(int, input()))
    li = [0]*10
    cnt = 0
    for k in A:
        li[k] += 1
    for m in range(len(li)):
        if li[m] >= cnt:
            ma = m
            cnt = li[m]
    print('#{0} {1} {2}'.format(i, ma, cnt))

    # T = int(input())
    # for i in range(1, T + 1):
    #     N = int(input())
    #     A = input()
    #     nums = [0] * N
    #     li = [0] * 10
    #     cnt = 0
    #     for j in range(len(A)):
    #         nums[j] = int(A[j])
    #     for k in nums:
    #         li[k] += 1
    #     for m in range(len(li)):
    #         if li[m] >= cnt:
    #             ma = m
    #             cnt = li[m]
    #     print('#{0} {1} {2}'.format(i, ma, cnt))
