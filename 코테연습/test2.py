def combo(depth):
    global MAX

    if depth == N or depth==M:
        cnt = 0
        for c in candies:
            cnt += len(set(c))
        MAX = max(MAX,cnt)
        return


    for i in range(1,M+1):
        if visit[i]:continue
        visit[i] = 1
        candies[depth].append(i)
        combo(depth+1)
        candies[depth].pop()
        visit[i]=0

for t in range(1,int(input())+1):
    N, M = map(int, input().split())
    candies = []
    MAX = 0
    for _ in range(N):
        info = list(map(int,input().split()))
        candy = []
        for c in range(1,len(info)):
            candy.append(info[c])
        candies.append(candy)
    visit = [0]*(M+1)
    combo(0)
    print("#{} {}".format(t,MAX))
