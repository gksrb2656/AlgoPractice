# T = int(input())
# for tc in range(1,T+1):
#     n = int(input())
#     visit = [0] * 10001
#     visit[0] = 1
#     visit[3] = 3
#     visit[6] = 13
#     if n>=9:
#         for i in range(9,n+1,3):
#             visit[i] = visit[i-9] - 3*visit[i-6] + 5*visit[i-3]
#             if visit[n]:
#                 break
#     print(visit[n]%1000000007)

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    visit = [0] * 10001
    visit[0] = visit[1] = visit[2] = 1
    visit[3] = 3
    for i in range(4,n+1):
        if i%3:
            visit[i] = visit[i-1] + visit[i-3]
        else:
            visit[i] = visit[i-3] + visit[i-1]*2
    print(visit)