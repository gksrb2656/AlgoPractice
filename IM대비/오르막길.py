N = int(input())
road = list(map(int, input().split()))
incline = []
s_p = []
d_p = []
cnt = 0
for i in range(len(road)-1):
    if road[i] < road[i+1]:
        cnt += 1
        if i+1 == len(road)-1:
            d_p.append(i+1)
            s_p.append(i - cnt+1)
    else:
        s_p.append(i-cnt)
        d_p.append(i)
        cnt = 0

for i in range(len(s_p)):
    incline.append(road[d_p[i]] - road[s_p[i]])
print(max(incline))
# for i in range(len(s_p)):
#     incline.append(road[d_p[i]]-road[s_p[i]])
#
# print(max(incline))