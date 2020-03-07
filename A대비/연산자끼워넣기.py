def permutation(k):
    global Max, Min, order
    if k == N - 1:
        s = numbers[0]
        for j in range(N - 1):
            if order[j] == '+':
                s += numbers[j + 1]
                continue
            if order[j] == '-':
                s -= numbers[j + 1]
                continue
            if order[j] == '*':
                s *= numbers[j + 1]
                continue
            if order[j] == '/':
                if s < 0 or numbers[j + 1] < 0:
                    s = -(s // -numbers[j + 1])
                else:
                    s = s // numbers[j + 1]
                continue
        if Min == '':
            Min = s
        elif Min > s:
            Min = s
        if Max == '':
            Max = s
        elif Max < s:
            Max = s

    for i in range(N - 1):
        if visit[i]: continue
        order += per[i]
        visit[i] = 1
        permutation(k + 1)
        order = order[:-1]
        visit[i] = 0


N = int(input())
numbers = list(map(int, input().split()))
cal = list(map(int, input().split()))

calculate = ['+', '-', '*', '/']
per = []
for i in range(4):
    per += calculate[i] * cal[i]

visit = [0] * (N - 1)
order = ''
permu = []
Max = ''
Min = ''
permutation(0)
print(Max)
print(Min)

# def dfs(k, n, add, sub, mul, div):
#     if k == N:
#         results.append(n)
#         return
#     if add != 0:
#         dfs(k + 1, n + num[k], add - 1, sub, mul, div)
#     if sub != 0:
#         dfs(k + 1, n - num[k], add, sub - 1, mul, div)
#     if mul != 0:
#         dfs(k + 1, n * num[k], add, sub, mul - 1, div)
#     if div != 0:
#         if n < 0: dfs(k + 1, -(-n // num[k]), add, sub, mul, div - 1)
#         else: dfs(k + 1, n // num[k], add, sub, mul, div - 1)
#
# N = int(input())
# num = list(map(int, input().split()))
# results = []
# dfs(1, num[0], *map(int, input().split()))
# print('{}\n{}'.format(max(results), min(results)))