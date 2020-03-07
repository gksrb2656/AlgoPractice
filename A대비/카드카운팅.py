T = int(input())
for t in range(1,T+1):
    Cards = list(input())
    deck = []
    dic = {}
    for i in range(len(Cards)//3):
        li = Cards[i*3:(i+1)*3]
        if li not in deck:
            deck.append(li)
        else:
            deck = []
            break
    for c in deck:
        if c[0] not in dic:
            dic[c[0]] = 12
        else:
            dic[c[0]] -= 1
    if len(dic) == 0:
        print('#{} ERROR'.format(t))
    elif len(dic) != 4:
        for k in range(4 - len(dic)):
            dic[k] = 13
    else:
        print("#{}".format(t), end=' ')
        for n in dic.values():
            print(n, end=' ')
        print()