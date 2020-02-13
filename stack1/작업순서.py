
for t in range(1,11):
    print("#{}".format(t), end =' ')
    visit = []
    V, E = map(int, input().split())
    node = list(map(int, input().split()))
    arr = []
    for i in range(E):
        arr.append(node[i*2:(i+1)*2])
    s_p = []
    e_p = []

    for i in range(len(node)):
        if i%2:
            e_p.append(node[i])
        else:
            s_p.append(node[i])

    for i in s_p:
        if e_p.count(i)==0 and i not in visit:
            visit.append(i)
            print(i, end =' ')

    while visit:
        a = visit.pop(-1)
        for j in arr:
            if a == j[0]:
                if e_p.count(j[1]) == 1:
                    visit.append(j[1])
                    print(j[1], end=' ')
                    e_p.remove(j[1])
                else:
                    e_p.remove(j[1])







