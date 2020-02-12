from copy import deepcopy
N, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in arr:
    i.append(i[0])
    i.pop(0)

arr_medal = deepcopy(arr)
arr_medal.sort(reverse=True)

for i in arr_medal:
    i.pop(3)

arr.sort(reverse=True)
for i in range(len(arr)):
    if arr[i][3] == C:
        k = arr[i][0:3]
        if arr_medal.count(k) > 1:
            for j in range(len(arr_medal)):
                if arr_medal[j] == k:
                    print(j+1)
                    break
        else:
            print(i+1)
# print(arr_medal)