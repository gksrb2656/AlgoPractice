memo = [0,1]

def fibo(n):
    global memo
    if n>=2 and len(memo) <=n:
        memo.append(fibo(n-1)+fibo(n-2))
    return memo[n]


k = fibo(10)
print(memo)

N = 10
memo2 = [-1]*(N+1)

memo2[0] = 0
memo2[1] = 1

def fibo2(N):
    if memo2[N] == -1:
        memo2[N] = fibo2(N-1)+fibo2(N-2)
    return memo2[N]

fibo2(N)
print(k)
print(memo2)

def fibo_dp(N):
    f = [0,1]
    for i in range(2,N+1):
        f.append(f[i-1] + f[i-2])

    return f[N]

k = fibo_dp(N)
print(k)