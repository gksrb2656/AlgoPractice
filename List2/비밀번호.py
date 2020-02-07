T = 10
for t in range(1, T+1):
    N, W = input().split()
    password = list(W)
    cnt = 0
    while 1:
        for i in range(len(password)-1):
            if password[i] == password[i+1]:
                password[i] = ''
                password[i + 1] = ''
                password = ''.join(password)
                password = list(password)
                cnt = 0
                break
            cnt += 1
        if cnt == len(password)-1:
            break
    print('#{} {}'.format(t, ''.join(password)))


