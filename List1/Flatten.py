for T in range(10):
    Dump = int(input())
    Boxes = list(map(int, input().split()))
    while max(Boxes)-1 > min(Boxes):
        Boxes[Boxes.index(max(Boxes))] -= 1
        Boxes[Boxes.index(min(Boxes))] += 1
        Dump -= 1
        if Dump == 0:
            break
    print('#{0} {1}'.format(T+1, max(Boxes)-min(Boxes)))

# for T in range(10):
#     Dump = int(input())
#     Boxes = list(map(int, input().split()))
#     while max(Boxes)-1 > min(Boxes):
#         for i in range(len(Boxes)):
#             if max(Boxes) == Boxes[i]:
#                 ma_idx = i
#             elif min(Boxes) == Boxes[i]:
#                 mi_idx = i
#         Boxes[ma_idx] -= 1
#         Boxes[mi_idx] += 1
#         Dump -= 1
#         if Dump == 0:
#             break
#     print(max(Boxes)-min(Boxes))

def min_search():
    min_Value = 101
    min_idx = -1
    for i in range(len(box)):
        if box[i] < min_Value:
            min_Value = box[i]
            min_idx = i
    return min_idx

def max_search():
    max_Value = 0
    max_idx = -1
    for i in range(len(box)):
        if box[i] > max_Value:
            max_Value = box[i]
            max_idx = i
    return max_idx

for tc in range(1,11):
    N = int(input())

    box = list(map(int, input().split()))

    for i in range(N):
        box[max_search()] -= 1
        box[min_search()] += 1

    print('#{} {}'.format(tc, box[max_search()]- box[min_search()]))

    #     maxIdx = 0
    #     maxValue = 0
    #     minIdx = 0
    #     minValue = 101
    #     for j in range(len(box)):
    #         if box[j] < minValue:
    #             minValue = box[j]
    #             minIdx = j
    #         if box[j] > maxValue:
    #             maxValue = box[j]
    #             maxIdx = j
    #     box[maxIdx] -= 1
    #     box[minIdx] += 1

