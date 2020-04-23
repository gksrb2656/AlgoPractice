for t in range(1,int(input())+1):
    N = int(input())
    arr = list(map(int,input().split()))
    nodes = [0]*(N+1)
    idx = 1
    for a in arr:
        flag = True
        idx_copy = idx
        while flag:
            if nodes[idx_copy//2]>a:
                nodes[idx_copy], nodes[idx_copy//2] = nodes[idx_copy//2], a
                idx_copy //= 2
            elif idx==idx_copy:
                nodes[idx] = a
                flag = False
            else:
                flag = False
        idx += 1
    ans = 0
    while N:
        ans += nodes[N//2]
        N//=2
    print("#{} {}".format(t,ans))

'''
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40
'''