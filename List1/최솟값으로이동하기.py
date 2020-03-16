T = int(input())
for t in range(1,T+1):
    W,H,N = map(int, input().split())
    cnt = 0
    r1,c1 = map(int, input().split())
    for i in range(1,N):
        r2,c2 = map(int, input().split())
        if r1<r2 and c1<c2:
            cnt += max(r2-r1,c2-c1)
        elif r1>r2 and c1>c2:
            cnt += max(r1 - r2, c1 - c2)
        else:
            cnt += abs(r2-r1)
            cnt += abs(c2-c1)
        r1,c1 = r2,c2
    print("#{} {}".format(t,cnt))