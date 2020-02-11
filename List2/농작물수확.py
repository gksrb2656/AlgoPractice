T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_t = 0
    for i in range(N):
        for j in range(N):
            sum_t += arr[i][j]
    sub_li = []
    sum_1 = 0
    sum_2 = 0
    sum_3 = 0
    for i in range(N-1):
        sum_1 = 0
        for j in range(N-1):
            sum_2 = 0
            for k in range(i+1):
                sum_1 += arr[k][j]
            for l in range(j+1, N):
                for m in range(N):
                    sum_2 += arr[m][l]
            sum_3 = sum_t - sum_1 - sum_2
            sub_li.append(max(sum_1,sum_2,sum_3)- min(sum_1, sum_2, sum_3))
    for i in range(N-1):
        sum_1 = 0
        for j in range(N-1,0,-1):
            sum_2 = 0
            for k in range(i+1):
                sum_1 += arr[k][j]
            for l in range(j,0,-1):
                for m in range(N):
                    sum_2 += arr[m][l-1]
            sum_3 = sum_t - sum_1 - sum_2
            sub_li.append(max(sum_1,sum_2,sum_3)- min(sum_1, sum_2, sum_3))
    print("#{} {}".format(t, min(sub_li)))

# def sum_farm(r1, c1, r2, c2):
#     tmp = 0
#     for i in range(r1, r2+1):
#         for j in range(c1, c2+1):
#             tmp += farm[i][j]
#     return tmp
# T = int(input())
# for t in range(T):
#     N = int(input())
#     farm = [list(map(int, input().split())) for _ in range(N)]
#     sum_list = []
#     for i in range(N-1):
#         for j in range(N-1):
#             sum_1 = sum_farm(0, 0, i, j)
#             sum_2 = sum_farm(i+1, 0, N-1, j)
#             sum_3 = sum_farm(0, j+1, N-1, N-1)
#             sum_list.append([sum_1, sum_2, sum_3])
#     find_min = 987654321
#     for i in range(len(sum_list)):
#         result = max(sum_list[i]) - min(sum_list[i])
#         if find_min > result:
#             find_min = result
#     print('#{} {}'.format(t+1,find_min))
