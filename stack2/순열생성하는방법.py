# arr = 'ABC'
# N = len(arr)
#
# for i in range(N):
#     for j in range(N):
#         if j == i: continue
#         for k in range(N):
#             if k == i or k == j: continue
#             print(arr[i], arr[j], arr[k])

arr = 'ABC'
N = len(arr)
visit = [0]*N  # 이전에 선택한 요소들에 대한 정보
order = []

def backtrack(k):   # K: 함수 호출 트리에서 높이, 선택한 요소의 수
    if k == N:      # 단말노드에 도착, 모든 선택이 끝났다.
        print(order)# order에 하나의 순열이 저장된 상태
    else:           # 아직 해야할 선택이 남은 상태
        for i in range(N):
            if visit[i]: continue
            visit[i] = 1
            order.append(arr[i])
            backtrack(k+1)
            order.pop()
            visit[i] = 0
backtrack(0)

# def backtrack(k, visit):
#     if k == N:
#         print(order)
#     else:
#         for i in range(N):
#             if visit & (1<<i): continue
#             order.append(arr[i])    # i번 요소를 선택
#             backtrack(k+1, visit | (1<<i))
#             order.pop()
# backtrack(0,0)

# arr = [i for i in range(11)]
# N = len(arr)
#
#
# bit = [0]*N
# def backtrack(k):
#     if k == N:
#         S = 0
#         for i in range(N):
#             if bit[i]: S += arr[i]
#         if S == 10:
#             for i in range(N):
#                 if bit[i]: print(arr[i], end=' ')
#     else:
#         bit[k] = 1; backtrack(k+1)
#         bit[k] = 0; backtrack(k+1)
# backtrack(0)



# arr = [i for i in range(1,11)]
# N = len(arr)
# A= []
#
# cnt = 0
# def backtrack(k, cur):
#     if cur > 10: return
#     if k == N:
#         global cnt
#         if cur == 10:
#             cnt += 1
#     else:
#         # A.append(arr[k])
#         backtrack(k + 1, cur + arr[k])
#         # A.pop()
#         backtrack(k + 1, cur)
#
# backtrack(0,0); print(cnt)