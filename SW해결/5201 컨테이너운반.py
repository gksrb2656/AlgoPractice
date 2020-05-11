for t in range(1,int(input())+1):
    N, M = map(int, input().split())
    Nw = list(map(int, input().split()))
    Mw = list(map(int, input().split()))
    Nw.sort()
    Mw.sort()
    ans = 0
    while Mw:
        Max = Mw.pop()
        for i in range(len(Nw)-1,-1,-1):
            if Nw[i]<=Max:
                ans += Nw[i]
                Nw.remove(Nw[i])
                break
    print("#{} {}".format(t, ans))