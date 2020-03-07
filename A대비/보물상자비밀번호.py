def DFS(k,li,n):
    if k == n:
        return
    for i in range(0,N,n):
        if int(li[i:i+n],16) not in numbers:
            numbers.append(int(li[i:i+n],16))
    a = li[-1]
    li = li[:N-1]
    li = a + li
    DFS(k+1,li,n)

T = int(input())
for t in range(1,T+1):
    N, K = map(int, input().split())
    n = N//4
    li = input()
    numbers = []
    DFS(0,li,n)
    numbers.sort(reverse=True)
    print(numbers)
    print("#{} {}".format(t,numbers[K-1]))



