arr = [69, 10, 30, 2, 16, 8, 31, 22]
sort = [0] * (len(arr))

#병합정렬
def mergeSort(lo, hi):
    if lo == hi: return

    mid = (lo + hi) // 2
    mergeSort(lo, mid)
    mergeSort(mid + 1, hi)

    i, j, k = lo, mid + 1, lo
    while i <= mid and j<= hi:
        if arr[i] < arr[j]:
            sort[k] = arr[i]; k,i = k+1, i+1
        else:
            sort[k] = arr[j]; k,j=k+1,j+1
    while i<=mid:
        sort[k]=arr[i]
        k,i = k+1, i+1
    while j<=hi:
        sort[k]=arr[j]
        k,j=k+1,j+1

    for i in range(lo, hi+1):
        arr[i] = sort[i]

mergeSort(0, len(arr) - 1)


def mergeSort(lst):
    if len(lst)==1:
        return lst

    mid = len(lst) // 2
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])

    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)

    return result

print(mergeSort(arr))

# 퀵정렬

