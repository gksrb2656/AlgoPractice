T = int(input())
for t in range(1,T+1):
    words = input()
    H = int(input())
    idx =list(map(int,input().split()))
    idx.sort()
    cnt = 0
    for i in range(H):
        if i>0 and idx[i-1]<=idx[i]:
            cnt += 1
        words = words[:idx[i]+cnt] +'-' + words[idx[i]+cnt:]
    print(words)