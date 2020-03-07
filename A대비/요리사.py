def sub(a, b, K):
    global s_s
    sum1 = 0
    sum2 = 0
    for i in range(K):
        for j in range(K):
            if i != j:
                sum1 += S[a[i]][a[j]]
    for i in range(K):
        for j in range(K):
            if i != j:
                sum2 += S[b[i]][b[j]]
    if s_s == -1:
        s_s = abs(sum1 - sum2)
    elif s_s > abs(sum1 - sum2):
        s_s = abs(sum1 - sum2)


def comb(k,n, K):
    if  k == K:
        sub(s1, s2, K)
        return

    for i in range(n, N):
        s2.remove(i)
        s1.append(i)
        comb(k+1, i+1, K)
        s1.pop()
        s2.append(i)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    S = [list(map(int, (input().split()))) for _ in range(N)]
    s2 = [i for i in range(N)]
    s1 = []
    s_s = -1
    comb(0,0, N // 2)
    print("#{} {}".format(t,s_s))


# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     S = [list(map(int, input().split())) for _ in range(N)]
#     ans = 0xffffffffff
#
#     for subset in range(1, 1 << N):
#         A, B = [], []
#         for i in range(N):
#             if subset & (1 << i):
#                 A.append(i)
#             else:
#                 B.append(i)
#
#         if len(A) != len(B): continue
#         sumA = sumB = 0
#         for i in range(len(A)):
#             for j in range(len(A)):
#                 sumA += S[A[i]][A[j]]
#                 sumB += S[B[i]][B[j]]
#         ans = min(ans, abs(sumA - sumB))
#
#     print('#{} {}'.format(tc, ans))