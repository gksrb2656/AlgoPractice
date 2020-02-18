def exp(C, n):
    if n == 0: return 1
    if n == 1: return C

    if n & 1:  # 홀수
        ret = exp(C, (n - 1)//2)
        return ret * ret * C
    else:
        ret = exp(C, n//2)
        return ret * ret

print(exp(2, 100))

print(20 >> 1)
print(20 >> 2)
print(20 << 1)
print(20 << 2)
print(21 << 1)
print(21 >> 1)

A = [64, 7, 4, 25, 10, 22, 11, 8]
N = len(A)
# def getMin(A, lo, hi):   # arr에서 최소값을 반화하는 함수
#     if lo == hi:
#         return A[lo]
#
#     ret = getMin(A, lo, hi - 1)
#     return min(ret, A[hi])
#
# print(getMin(A, 0, N-1))

def getMin(A, lo, hi):
    if lo == hi:
        return A[lo]

    mid = (lo + hi) >> 1
    l = getMin(A, lo, mid)
    r = getMin(A, mid+1, hi)
    return min(l, r)