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

