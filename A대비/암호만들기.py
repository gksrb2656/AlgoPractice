def comb(k,n):
    if k == N:
        cnt1 = 0
        cnt2 = 0
        for j in order:
            if j in 'aeiou':
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1>=1 and cnt2>=2:
            for i in order:
                print(i, end ='')
            print()
        return

    for i in range(n,M):
        order.append(li[i])
        comb(k+1,i+1)
        order.pop()

N, M = map(int,input().split())
li = input().split()
li.sort()
order = []
comb(0,0)