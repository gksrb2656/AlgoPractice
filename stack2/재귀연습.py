# for i in range(3):
#     print('hello')
#
# def printHello():
#     printHello()
#     print('hello')
#
# printHello()

# cnt = 0
# def printHello(i,n):
#     if i == n:
#         global cnt
#         cnt += 1
#     else:
#         printHello(i, n+1)
#         printHello(i, n+1)

# 부분집합
# path = [0] * 3
# a = 'ABC'
# def printHello(i, n):
#     if i == n:
#         print(path)
#     else:
#         path[i] = 1
#         printHello(i+1, n)
#
#         path[i] = 0
#         printHello(i+1, n)
#
# printHello(0, 3)

# N = 3
# bit = [0]*N
# P_s = []
# def subset(k, n):
#     if k == n:
#         a = bit[:]
#         P_s.append(a)
#         print(bit)
#     else:
#         for i in range(2):
#             bit[k] = i
#             subset(k+1, n)
#
# subset(0,N)
# print(P_s)

# path = []
# def backtrack(k, n):
#     if n < 0: return
#     if n == 0:
#         print(path)
#     else:
#         path.append('l'); backtrack(k+1, n-1); path.pop()
#
#         path.append('='); backtrack(k + 1, n-2); path.pop()
#
#         path.append('II'); backtrack(k + 1, n - 2); path.pop()
#
# backtrack(0, 4)

combo = []
def combination(arr, r):
    # 1.
    arr = sorted(arr)

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            c = chosen[:]
            print(c)
            return combo.append(c)

    	# 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])

combination('ABCDE', 2)
# combination([1, 2, 3, 4, 5], 3)

print(combo)