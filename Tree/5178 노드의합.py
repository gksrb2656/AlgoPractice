for t in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    arr = [0 for _ in range(N+1)]
    for _ in range(M):
        node, value = map(int, input().split())
        arr[node] = value
    def DFS(n,cnt, data):
        if n>1:
            if cnt*2<=N:
                DFS(int(n//2),cnt*2,data)
                if cnt*2+1<=N:
                    DFS(int(n//2),cnt*2+1,data)
                else:
                    arr[cnt//2] += arr[cnt]
                    return
            if cnt>1:
                arr[cnt//2] += arr[cnt]
                return
        else:
            arr[cnt//2] += arr[cnt]
    DFS(N,1,0)
    print("#{} {}".format(t,arr[L]))