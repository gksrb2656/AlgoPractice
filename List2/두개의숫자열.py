import sys
sys.stdiin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Max = 0
    if N > M:
        for i in range(N-M+1):
            summ = 0
            for j in range(i, M+i):
                summ += A[j]*B[j-i]
                print(summ)
                print(A[j], B[j-i])
            if Max <= summ:
                Max = summ
    elif N < M:
        for i in range(M-N+1):
            summ = 0
            for j in range(i, N+i):
                summ += A[j-i]*B[j]
            if Max <= summ:
                Max = summ
    # print(Max)
