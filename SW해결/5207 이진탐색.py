for t in range(1,int(input())+1):
    l_A, l_B = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    ans = 0
    for b in B:
        lo,hi = 0, l_A-1
        switch = 0
        while lo<=hi:
            mid = (lo+hi)//2
            if b == A[mid]:
                ans += 1
                break

            elif b < A[mid]:
                if switch==1:break
                hi = mid-1
                switch = 1
            else:
                if switch==-1:break
                lo = mid+1
                switch = -1
    print("#{} {}".format(t,ans))