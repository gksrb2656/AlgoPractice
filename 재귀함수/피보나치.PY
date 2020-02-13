def fibo(n):
    global cnt
    cnt += 1
    if n <= 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

cnt = 0
k = fibo(5)
print(k, cnt)