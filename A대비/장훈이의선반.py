def comb(k,n,sum_h):
    global ans
    if B<=sum_h:
        if ans>sum_h-B:
            ans = sum_h-B
        return

    for i in range(n,N):
        sum_h += heights[i]
        comb(k+1,i+1,sum_h)
        sum_h -= heights[i]

T = int(input())
for t in range(1,T+1):
    N, B = map(int,input().split())
    heights = list(map(int,input().split()))
    ans = sum(heights)
    p = N
    comb(0,0,0)
    print("#{} {}".format(t,ans))