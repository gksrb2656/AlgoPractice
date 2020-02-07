T = int(input())
for i in range(1,T+1):
    N = int(input())
    li = list(map(int,input().split()))
    li2=[]
    for j in range(len(li)//2):
        li2.append(max(li))
        li.remove(max(li))
        li2.append(min(li))
        li.remove(min(li))
    li2 = list(map(str, li2[:10]))
    print("#{0} {1}".format(i, ' '.join(li2)))

# T = int(input())
# for i in range(1,T+1):
#     N = int(input())
#     li = list(map(int,input().split()))
#     Max = 0
#     li2 = []
#     for _ in range(len(li)):
#         for j in li:
#             if j not in li2:
#                 if Max == 0:
#                     Max = j
#                 elif Max < j:
#                     Max = j
#             li2.append(Max)
#     li3 = []
#     for length in range(len(li)//2):
#         li3.append(li2[len(li)-length-1])
#         li3.append(li2[length])
#     print(li3)

