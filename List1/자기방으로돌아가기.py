T = int(input())
for t in range(1,T+1):
    N = int(input())
    visit = [0]*401
    for i in range(N):
        r1, r2 = map(int,input().split())
        cnt = 0
        ep = max(r1, r2)
        sp = min(r1, r2)
        if ep%2:
            ep += 1
        if not sp%2:
            sp -= 1
        for j in range(sp,ep+1):
            visit[j] += 1
    print("#{} {}".format(t,max(visit)))

