def per(k):
    if k == M:
        c = order[:]
        p_s.append(tuple(c))
        return

    for i in range(N):
        if v[i]: continue
        v[i] = 1
        order.append(li[i])
        per(k+1)
        order.pop()
        v[i] = 0

N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort() #순서대로 나오게 정렬 먼저
v = [0]*N
order = []
p_s = []
per(0)
p_s =  sorted(list(set(p_s)))

for numbers in p_s:
    for num in numbers:
        print(num, end=' ')
    print()
