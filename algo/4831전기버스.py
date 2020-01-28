import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
for i in range(T):
    cnt = 0
    K, N, M = map(int, input().split())
    nxt = K
    charge = list(map(int, input().split()))
    for j in range(M):
        if charge[j] == nxt:
            nxt += K
            cnt += 1
        elif charge[j] > nxt:
            if charge[j-1]+K < charge[j]:
                cnt = 0
                break
            else:
                nxt = charge[j-1]+K
                cnt += 1
        if j == M-1:
            if nxt < N:
                if (charge[j] + K) >= N:
                    cnt += 1
                else:
                    cnt = 0
    print("#{0} {1}".format(i+1, cnt))
