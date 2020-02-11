C, R = map(int, input().split())
N = int(input())
li = []
row = [0,R]
cal = [0,C]
width = []
for i in range(N):
    li.append(list(map(int, input().split())))
for i in range(len(li)):
    if li[i][0] == 0:
        row.append(li[i][1])
    else:
        cal.append(li[i][1])
row.sort()
cal.sort()
# print(row,cal)
for r in range(len(row)-1):
    for c in range(len(cal)-1):
        width.append((cal[c+1]-cal[c])*(row[r+1] - row[r]))
print(max(width))
