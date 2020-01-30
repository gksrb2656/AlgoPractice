T = int(input())
for i in range(1,T+1):
    N = int(input())
    li = list(map(int,input().split()))
    li2=[]
    for j in range(len(li)//2):
        li2.append(max(li))
        li.remove(max(li))
        li2.append(min(li))
        li.remove(min(li))
    li2 = list(map(str, li2[:10]))
    print("#{0} {1}".format(i, ' '.join(li2)))