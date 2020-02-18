# def quick(st, ed):
#     if st == ed:
#         return st
#     x = quick(st, (st + ed) // 2)
#     y = quick((st + ed) // 2 + 1, ed)
#     return win(x, y)
# def win(a, b):
#     if (li[a - 1] == 1 and li[b - 1] == 2) or (li[a - 1] == 2 and li[b - 1] == 3) or (
#             li[a - 1] == 3 and li[b - 1] == 1):
#         return b
#     if (li[a - 1] == 1 and li[b - 1] == 1) or (li[a - 1] == 2 and li[b - 1] == 2) or (
#             li[a - 1] == 3 and li[b - 1] == 3):
#         return a
#     return a

# T = int(input())
# for tc in range(1, T + 1):
#     n = int(input())
#     li = list(map(int, input().split()))
#     st = 1
#     ed = n
#     print('#{} {}'.format(tc, quick(st, ed)))

def devide(lo, hi):
    if lo == hi:
        return lo

    l = devide(lo, (lo+hi)//2)
    h = devide((lo+hi)//2+1, hi)
    return game(l, h)

def game(l, h):
    if arr[l] != 3 and arr[h] != 3:
        if arr[l] == max(arr[l], arr[h]):
            return l
        else:
            return h
    if arr[l] != 1 and arr[h] != 1:
        if arr[l] == max(arr[l], arr[h]):
            return l
        else:
            return h
    if arr[l] != 2 and arr[h] != 2:
        if arr[l] == min(arr[l], arr[h]):
            return l
        else:
            return h



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    print("#{} {}".format(tc, devide(0, N-1)+1))