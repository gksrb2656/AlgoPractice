T = int(input())
for t in range(1, T+1):
    result = ''
    li = [input() for _ in range(5)]
    max_len = 0
    for l in li:
        if len(l) > max_len:
            max_len = len(l)
    for i in range(max_len):
        for j in range(5):
            if len(li[j]) < i+1:
                continue
            result += li[j][i]
    print('#{} {}'.format(t, result))