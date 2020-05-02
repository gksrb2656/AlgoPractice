def binary(num):
    global ans, cnt
    while 1:
        num *=2
        ans += str(int(num) % 2)
        cnt+=1
        if num % 1 == 0:
            break
    return

for tc in range(1, int(input())+1):
    num = float(input())
    ans = ''
    cnt = 0
    binary(num)

    if cnt > 13:
        print('#{} overflow'.format(tc))
    else:
        print('#{} {}'.format(tc, ans))