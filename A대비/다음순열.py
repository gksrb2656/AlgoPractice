# def per(k):
#     if k == N:
#         print(*order)
#         return
#
#     for i in arr_sort:
#         if i in order: continue
#         order.append(i)
#         per(k+1)
#         order.pop()
#
# all_per = []
# N = int(input())
# arr = list(map(int, input().split()))
# arr_sort = sorted(arr)
# order = []
# per(0)
# print(all_per)

N = int(input())
arr = list(map(int, input().split()))
arr_revserse = sorted(arr, reverse=True)
compare = [N-1]
flag = False
if arr == arr_revserse:
    print(-1)
else:
    for j in range(N-2,-1,-1):
        for i in compare:
            if arr[i]>arr[j]:
                flag = True
                a = arr.pop(i)
                arr_back= arr[j:]
                arr_back.sort()
                arr = arr[:j] + [a] + arr_back
                break
        compare.append(j)
        if flag:break
    print(*arr)


# flag = True
# for i in range(N-1):
#     if arr[i]<arr[i+1]:
#         flag = False
#     if not flag:
#         if arr[i]>arr[i+1]:
#                 ep = i
#                 break