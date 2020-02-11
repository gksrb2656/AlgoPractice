N = int(input())
switch = list(map(int,input().split()))
people = int(input())
li = []
for i in range(people):
    li.append(list(map(int, input().split())))

for i in range(len(li)):
    if li[i][0] == 1:
        for j in range(len(switch)):
            if (j+1) % li[i][1] == 0:
                if switch[j] != 0:
                    switch[j] = 0
                else:
                    switch[j] = 1
    else:
        n = li[i][1] - 1
        k = min(n, len(switch)-n-1)
        idx = 0
        if 0<n<len(switch)-1:
            for j in range(k+1):
                if switch[n-j] == switch[n+j]:
                    idx = j
                else:
                    break
        for l in range(n-idx,n+idx+1):
            if switch[l] != 0:
                switch[l] = 0
            else:
                switch[l] = 1
for i in range(len(switch)-1):
    print(switch[i], end =' ')
    if (i+1)%20 == 0 and i != 1:
        print()
print(switch[-1], end ='')
