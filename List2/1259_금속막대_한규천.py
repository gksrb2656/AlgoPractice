T = int(input())
for t in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    boy = [li[i] for i in range(2*N) if i%2==0]
    girl = [li[i] for i in range(2*N) if i % 2]
    # print(boy)
    # print(girl)
    # g_b = [[0,0] for _ in range(N)]
    # for i in range(N):
    #     g_b[i][0] = boy[i]
    #     g_b[i][1] = girl[i]
    lenth = []
    for i in range(N):
        for j in range(N):
            if len(lenth) != 0:
                if lenth[-1] == boy[i]:
                    lenth.append(boy[i])
                    lenth.append(girl[i])
                elif lenth[0] == girl[j]:
                    lenth[0](girl[j])
                    lenth[0](boy[j])
            elif boy[i] == girl[j]:
                lenth.append(boy[j])
                lenth.append(girl[j])
                # lenth.append(boy[i])
                # lenth.append(girl[i])
    lenth = list(map(str, lenth))
    print(' '.join(lenth))

# 10
# 3
# 3 4 2 3 4 5
# 4
# 1 2 5 1 2 4 4 3