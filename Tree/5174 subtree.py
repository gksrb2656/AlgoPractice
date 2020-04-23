for t in range(1,int(input())+1):
    E, N = map(int, input().split())
    connect = list(map(int, input().split()))
    arr = [[] for _ in range(E+2)]
    for i in range(0,2*E,2):
        arr[connect[i]].append(connect[i+1])

    root = N
    ans = 1
    def DFS(root):
        global ans
        while 1:
            if arr[root]:
                ans += len(arr[root])
                if len(arr[root])>1:
                    DFS(arr[root][0])
                    DFS(arr[root][1])
                    return
                else:
                    DFS(arr[root][0])
                    return
            else:
                return
    DFS(N)
    print("#{} {}".format(t,ans))