#다익스트라
# V,E = map(int, input().split())
# adj = {i:[] for i in range(V)}
# for i in range(E):
#     s,e,c = map(int,input().split())
#     adj[s].append([e,c])
#     #adj[e].append([s,c])
#
# INF = float('inf')
# dist = [INF]*V
# selected = [False]*V
#
# dist[0] = 0
# cnt = 0
# while cnt<V:
#     min = INF
#     u = -1
#     for i in range(V):
#         if not selected[i] and dist[i] < min:
#             min = dist[i]
#             u = i
#     #결정
#     selected[u] = True
#     cnt += 1
#     #간선완화
#     for w, cost in adj[u]: #도착정점, 가중치
#         if dist[w]>dist[u]+cost:
#             dist[w] = dist[w]+cost
# print(dist)



##프림
'''
7 11
0 5 60
0 1 32
0 2 31
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

'''
output
[0,21,31,34,46,18,25]
175
'''


# V,E = map(int,input().split())
# adj = [[0]*V for _ in range(V)]
# for i in range(E):
#     s,e,c = map(int,input().split())
#     adj[s][e] = c
#     adj[e][s] = c
# '''
# for row in adj:
#     print(row)
# [0, 32, 31, 0, 0, 60, 51]
# [32, 0, 21, 0, 0, 0, 0]
# [31, 21, 0, 0, 46, 0, 25]
# [0, 0, 0, 0, 34, 18, 0]
# [0, 0, 46, 34, 0, 40, 51]
# [60, 0, 0, 18, 40, 0, 0]
# [51, 0, 25, 0, 51, 0, 0]
# '''
# # key,p,mst 준비
# INF = float('inf')
# key = [INF] * V
# p = [-1]*V
# mst = [0]*V
#
# # 시작점 선택 : 0번 선택
# key[0] = 0
# cnt = 0
# result = 0
# while cnt < V:
#     # 아직 mst가 아니고 key가 최소인 정점 선택 : u
#     min = INF
#     u = -1
#     for i in range(V):
#         if not mst[i] and key[i] < min:
#             min = key[i]
#             u = i
#     # u를 mst 로 선택
#     mst[u] = 1
#     result += min
#     cnt += 1
#     # key값을 갱신
#     # u에 인접하고 아직 mst가 아닌 정점 w에서 key[w] > u-w 가중치면 갱신
#     for w in range(V):
#         if adj[u][w] > 0 and not mst[w] and key[w] > adj[u][w]:
#             key[w] = adj[u][w]
#             p[w] = u
# print(key)
# print(p)
# print(result)


##이진힙 프림
'''
7 11
0 5 60
0 1 32
0 2 31
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

'''
output
[0,21,31,34,46,18,25]
175
'''
# import heapq
#
# V,E = map(int,input().split())
# adj = {i:[] for i in range(V)}
# for i in range(E):
#     s,e,c = map(int,input().split())
#     adj[s].append([e,c])
#     adj[e].append([s,c])
# # print(adj)
# # key, mst, 우선순위큐 준비
# INF = float('inf')
# key = [INF] * V
# mst = [0]*V
# pq = []
# # 시작 정점 선택 : 0
# key[0] = 0
# # 큐에 모든 정점을 넣음 but 이 코드는 큐에 시작정점만 넣음(key,정점인덱스를 둘 다 넣음)
# # 우선순위 큐 -> 이진 힙 사용 heapq
# heapq.heappush(pq,(0,0))  # 우선순위 : 원소의 첫번째 요소인데, 우선순위(가중치=key)에 따라 가져올것(key,정점)
# result = 0
# while pq:
#     # 최솟값 찾기
#     k,node = heapq.heappop(pq)
#     if mst[node] : continue
#     # mst로 선택
#     mst[node] = 1
#     result += k
#     # key값 갱신 -> key배열/큐 둘다 갱신
#     for dest,wt in adj[node]:  # dest: 가고싶은 곳, wt: 가중치
#         if not mst[dest] and key[dest]>wt:
#             key[dest] = wt
#             # 큐 갱신 -> (key,정점) -> 1. 수정하거나 2. 새로운 (key,정점)을 삽입하고 필요없는 원소는 스킵하거나..
#             heapq.heappush(pq,(key[dest],dest))
#
# print(result)



## 크루스칼
'''
7 11
0 5 60
0 1 32
0 2 31
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

'''
output
[[3,5,18],[1,2,21],[2,6,25],[0,2,31],[3,4,34],[2,4,46]]
175
'''
# def make_set(x):
#     p[x] = x
#
# def find_set(x):
#     if p[x] == x: return x
#     return find_set(p[x])
#
# def union(x,y):
#     px= find_set(x)
#     py = find_set(y)
#     if rank[px] > rank[py]:
#         p[py] = px
#     else:
#         p[px] = py
#         if rank[px] == rank[py]:
#             rank[py] += 1
#
# V,E = map(int,input().split())
# edges = [list(map(int,input().split())) for i in range(E)]
# # print(edges)
# # 간선을 간선가중치를 기준으로 정렬
# edges.sort(key=lambda x:x[2])
# # print(edges)
# # MAKE_SET : 모든 정점에 대해 집합 생성
# p = [0]*V
# rank = [0]*V
# for i in range(V):
#     make_set(i)
#
# cnt = 0
# result = 0
# mst=[]
# # 모든 간선에 대해서 반복 -> V-1개의 간선이 선택될 때까지
# for i in range(E):
#     s,e,c = edges[i][0],edges[i][1],edges[i][2]
#     # 사이클이면 스킵 : 간선의 두 정점이 서로 같은 집합이면 -> FIND_SET
#     if find_set(s) == find_set(e) : continue
#     # 간선 선택
#     # -> mst에 간선 정보 더하기 / 두 정점을 합친다 -> UNION
#     result += c
#     mst.append(edges[i])
#     union(s,e)
#     cnt+=1
#     if cnt == V-1 : break
#
# print(result)
# # print(mst)




## 다익스트라
'''
6 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6
'''

'''
output
[0,3,5,9,11,12]
'''
# # dist, selected 배열 준비
# # 시작점 선택
# # 모든 정점이 선택될 때까지
# # 아직 선택되지 않고, dist값이 최소인 정점 : u
# # 정점 u의 최단거리 결정
# # 정점 u에 인접한 정점에 대해서 간선 완화
# V, E = map(int, input().split())
# adj = {i: [] for i in range(V)}
# for i in range(E):
#     s, e, c = map(int, input().split())
#     adj[s].append([e, c])
#
# INF = float('inf')
# dist = [INF] * V
# selected = [0] * V
#
# dist[0] = 0
# cnt = 0
# while cnt < V:
#     # dist가 최소인 정점 찾기
#     min = INF
#     u = -1
#     for i in range(V):
#         if not selected[i] and dist[i] < min:
#             min = dist[i]
#             u = i
#     # 결정
#     selected[u] = 1
#     cnt += 1
#     # 간선 완화
#     for w,cost in adj[u]: # 도착정점, 가중치
#         if dist[w] > dist[u]+cost:
#             dist[w] = dist[u] + cost
# print(dist)


