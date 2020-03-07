hobits = []
N = []
order = []
def find_hobit(k,n):
    global hobits
    if k == 7:
        if sum(order) == 100:
            hobits = order[:]
            return
    for i in range(n,9):
        order.append(N[i])
        find_hobit(k+1,i+1)
        order.pop()

for i in range(9):
    N.append(int(input()))
find_hobit(0,0)
hobits.sort()
for i in hobits:
    print(i)
