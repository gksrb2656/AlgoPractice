import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    li = input().split()
    stick = list()
    visit = list()
    boy = [li[i] for i in range(2*N) if not i%2]
    girl = [li[i] for i in range(2 * N) if i%2]
    for i in range(N):
        cnt = 0
        for j in range(N):
            if i != j:
                if boy[i] != girl[j]:
                    cnt += 1
        if cnt == N-1:
            alone = boy[i]
            stick.append(boy[i])
            stick.append(girl[i])
            visit.append(i)
            break
    while len(visit) != N:
        for i in range(N):
            if i not in visit:
                if stick[-1] == boy[i]:
                    stick.append(boy[i])
                    stick.append(girl[i])
                    visit.append(i)
                    break
    print("#{} {}".format(t, stick))



