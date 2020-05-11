def search():
    st=ed=0
    ss=arr[0]
    answer = N+1
    while ed<N:
        if ss>= S:
            if answer>=ed-st+1:
                answer = ed-st+1
            ss-=arr[st]
            st += 1
        else:
            ed += 1
            if ed<=N-1:
                ss += arr[ed]
    return answer

N, S = map(int,input().split())
arr = list(map(int, input().split()))
ans = search()
if ans>N:
    print(0)
else:
    print(ans)
