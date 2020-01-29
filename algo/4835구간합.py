# import sys
# sys.stdin = open("sample_input.txt", "r")
# T = int(input())
T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    for j in range(N-M+1):
        sums = 0
        for k in range(M):
            sums += li[j+k]
        if j == 0:
            mi = sums
            ma = sums
        if sums > ma:
            ma = sums
        if sums < mi:
            mi = sums
    print('#{0} {1}'.format(i+1, ma - mi))