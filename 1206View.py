import sys
sys.stdin = open("input.txt", "r")
for i in range(10):
    counts = 0
    size = int(input())
    T = list(map(int, input().split()))
    for j in range(2, size-2):
        nums = T[j]
        for k in [j-2, j-1, j+1, j+2]:
                if T[j] > T[k]:
                    if (T[j] - T[k]) < nums:
                        nums = T[j] - T[k]
                else:
                    nums = 0
        counts += nums
    print('#{0} {1}'.format(i+1, counts))
