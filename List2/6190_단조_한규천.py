# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     li = list(map(int, input().split()))
#     Danjo = []
#     for i in range(N-1):
#         for j in range(i+1,N):
#             cnt1 = 1
#             cnt2 = 1
#             num = li[i] * li[j]
#             while num > 1:
#                 cnt2 += 1
#                 n1 = num % 10
#                 num = num//10
#                 n2 = num % 10
#                 if n1 < n2:
#                     break
#                 else:
#                     cnt1 += 1
#             if cnt1 == cnt2:
#                 Danjo.append(li[i] * li[j])
#     if len(Danjo) == 0:
#         print('-1')
#     print(max(Danjo))

T = int(input())
for t in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    Danjo = []
    cnt  = 0
    for i in range(N-1):
        for j in range(i+1, N):
            num = li[i] * li[j]
            D = list(str(num))
            # print(D)
            for d in range(len(D)-1):
                if D[d] <= D[d+1]:
                    cnt += 1
                else:
                    break
            if cnt == len(D)-1:
                Danjo.append(num)
            cnt = 0
    if len(Danjo)==0:
        print(-1)
    else:
        print(max(Danjo))