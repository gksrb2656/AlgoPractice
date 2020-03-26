# def per(k, M):
#     if k == M:
#         return print(order)
#
#     for i in range(1,N+1):
#         if visit[i-1]: continue
#         if order and order[-1]>i:continue
#         order.append(i)
#         visit[i-1] = 1
#         per(k + 1,M)
#         order.pop()
#         visit[i-1] = 0
#
#
# N=4
# M=2
# order = []
# visit = [0]*N
# per(0,M)
# N = 6
# order = []
# def comb(k,n,K):
#     if k == K:
#         print(*order)
#         return
#
#     for i in range(n + 1, N + 1):
#         order.append(i)
#         comb(k+1,i, K)
#         order.pop()
#
# comb(0,0,3)

# def solution(cache_size, cities):
#     time = 0
#     cache_array = [' '] * cache_size
#
#     for city in cities:
#         city_lowered = city.lower()
#         if city_lowered in cache_array:
#             time = time + 1
#             cache_array.remove(city_lowered)
#             cache_array.append(city_lowered)
#         else:
#             time += 5
#             cache_array.append(city_lowered)
#             cache_array.pop(0)
#         print(cache_array)
#     return time
#
# solution(3,['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'])

# for i in range(16):
#     for j in range(4):
#         if i&(1<<j):
#             print(True,i,j,i&(1<<j))
#         else:
#             print(False,i,j,i&(1<<j))

# T = int(input())
# for t in range(1,T+1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#     n = 0
#     S = nums[0]
#     Max = S
#     for i in range(1,N):
#         if S+nums[i]<0 or S<0:
#             S = nums[i]
#         else:
#             S += nums[i]
#         if S>Max:
#             Max = S
#     print("#{} {}".format(t,Max))

##***kruscal알고리즘***
# def solution(n, costs):
#     costs.sort()
#     connect=[costs[0][0]]
#     answer = 0
#     while len(connect)!=n:
#         temp=1000000000000000
#         idx=0
#         for i in range(len(costs)):
#             if costs[i][0] in connect or costs[i][1] in connect:
#                 if costs[i][0] in connect and costs[i][1] in connect:
#                     continue
#                 if temp > costs[i][2]:
#                     temp=costs[i][2]
#                     idx=i
#         answer+=temp
#         connect.append(costs[idx][0])
#         connect.append(costs[idx][1])
#         connect=list(set(connect))
#         costs.pop(idx)
#     return answer

# def solution(N, number):
#     S = [0, {N}]
#     for i in range(2, 9):
#         case_set = {int(str(N)*i)}
#         for i_half in range(1, i//2+1):  # S[i_half] S[1]
#             for x in S[i_half]:
#                 for y in S[i-i_half]:
#                     case_set.add(x+y)
#                     case_set.add(x-y)
#                     case_set.add(y-x) # y-x 케이스 추가
#                     case_set.add(x*y)
#                     if x != 0:
#                         case_set.add(y//x)
#                     if y != 0:
#                         case_set.add(x//y)
#         if number in case_set:
#             return i
#         S.append(case_set)
#         print(S)
#     return -1
#
#
# print(solution(5, 12))


