for t in range(1, int(input())+1):
    N = int(input())
    level = 0
    N_copy = N
    while N_copy>1:
        N_copy //= 2
        level += 1
    arr = [0 for _ in range(N+1)]
    data = 1
    def DFS(n,cnt):
        global data
        if n>1:
            if cnt*2<=N:
                DFS(int(n//2),cnt*2)
            arr[cnt] = data
            data += 1
            if cnt*2+1<=N:
                DFS(int(n//2)+1,cnt*2+1)
        elif n==1:
            arr[cnt]=data
            data+=1
        elif n==2:
            arr[cnt]=data
            data+=1
    DFS(2**level,1)
    print("#{} {} {}".format(t,arr[1], arr[N//2]))