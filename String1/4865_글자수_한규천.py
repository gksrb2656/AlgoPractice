T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()
    dic = {}
    for i in str2:
        if i in str1:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
    print('#{} {}'.format(t, max(dic.values())))
