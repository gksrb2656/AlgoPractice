def dfs(k, n, add, sub, mul, div):
    if k == N:
        results.append(n)
        return
    if add != 0:
        dfs(k + 1, n + num[k], add - 1, sub, mul, div)
    if sub != 0:
        dfs(k + 1, n - num[k], add, sub - 1, mul, div)
    if mul != 0:
        dfs(k + 1, n * num[k], add, sub, mul - 1, div)
    if div != 0:
        if n < 0: dfs(k + 1, -(-n // num[k]), add, sub, mul, div - 1)
        else: dfs(k + 1, n // num[k], add, sub, mul, div - 1)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    results = []
    cal = list(map(int, input().split()))
    num = list(map(int, input().split()))
    dfs(1, num[0],*cal)
    print('#{} {}'.format(t,max(results)-min(results)))