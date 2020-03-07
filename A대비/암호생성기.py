from collections import deque

# def DFS():

T = int(input())
for t in range(1,10):
    password = deque(map(int, input().split()))
    cnt = 0
    while 1:
        cnt = (cnt + 1) % 6
        if cnt == 0:
            cnt = 1
        a = password.popleft()
        if a - cnt<= 0:
            a = 0
        else:
            a -= cnt
        password.append(a)
        if a == 0:
            break

    print('#{}'.format(t), *password)