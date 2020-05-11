def permu(depth):
    if depth==N:
        perm_set.append(perm[:]+[0])
        return

    for i in range(1,N):
        if i in perm:continue
        perm.append(i)
        permu(depth+1)
        perm.pop()

for t in range(1,int(input())+1):
    N = int(input())
    perm = [0]
    perm_set = []
    permu(1)
    ans = 10**6
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in perm_set:
        s = 0
        flag = 0
        for j in range(N):
            s += arr[i[j]][i[j+1]]
            if s>=ans:
                flag=1
                break
        if flag:continue
        ans = min(s,ans)
    print("#{} {}".format(t,ans))