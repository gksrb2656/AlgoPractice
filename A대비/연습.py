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


arr =[[0]*11 for _ in range(11)]
r,c = 3,3
rg = 3
for i in range(1,11):
    for j in range(1,11):
        if abs(r-i)+abs(c-j) <= 3:
            arr[i][j] += 1
for jj in arr:
    print(jj)