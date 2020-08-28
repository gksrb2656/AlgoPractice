def find_set(v):
    if v == memo[v]:
        return v
    memo[v] = find_set(memo[v])
    return memo[v]

def union(x,y):
    X = find_set(x)
    Y = find_set(y)

    if X != Y:
        memo[Y] = X

for t in range(1,int(input())+1):
    N, M = map(int, input().split())
    memo = [i for i in range(N + 1)]
    arr = list(map(int, input().split()))
    for i in range(0,M*2,2):
        union(arr[i],arr[i+1])
    for i in range(1,N+1):
        find_set(i)
    memo = set(memo)
    print("#{} {}".format(t, len(memo)))
