T = int(input())
for t in range(1, T+1):
    N = int(input())
    pascal = [[]]
    for i in range(N):
        li = [1]
        for j in range(len(pascal[i])):
            if j == len(pascal[i])-1:
                li.append(1)
            else:
                li.append(pascal[i][j]+pascal[i][j+1])
        pascal.append(li)
    print('#{}'.format(t))
    for k in range(1,len(pascal)):
        for l in pascal[k]:
            print(l, end =' ')
        print()
