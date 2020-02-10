T = int(input())
nums = ['ZRO', "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for t in range(1, T+1):
    s = ''
    tc, N = input().split()
    print(tc)
    numbers = input()
    li = numbers.split()
    for i in nums:
        for j in li:
            if i == j:
                s += j + ' '
    print(s[:len(s)-1])

