T = int(input())
for t in range(1, T+1):
    cnt = 0
    bit = list(map(int, input()))
    for i in range(len(bit)-1):
        if bit[0] == 1:
        	cnt += 1
        	if bit[i] != bit[i+1]:
                    cnt += 1
        else:
            if bit[i] != bit[i+1]:
                cnt += 1
    print('#{} {}'.format(t, cnt))