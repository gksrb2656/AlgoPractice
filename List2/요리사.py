# T = int(input())


# for i in range(5):
#     for j in range(i+1,5):
#         for k in range(j+1,5):
#             print(i,j,k)


# combo = []
# arr = 'ABCDE'
# N = len(arr)
# R=3
# pick=[0]*R
# def comb(k,s):#k-depth s - 반복의 시작위치
#     if k == R:
#         return
#     for i in range(s,N):
#         pick[k] =i
#         comb(k+1,i+1)
#     combo.append(pick)
#
# comb(0,0)
# print(combo)

# for t in range(1, T+1):
#     N = int(input())
#     Synergy = [list(map(int, input().split())) for _ in range(N)]
#     combo = [[0]*N for _ in range(N)]
#     K = N/2

# import copy
#
# s_s = []
# def everySubset(oriSet, subSet=[], last=0):
#     print(subSet)
#     s_s.append(subSet)
#     if last == len(oriSet) + 1:
#         return
#
#     for i in range(last, len(oriSet)):
#         next_subSet = copy.deepcopy(subSet)
#         next_subSet.append(oriSet[i])
#         everySubset(oriSet, next_subSet, i + 1)
#
#
# if __name__ == '__main__':
#     oriSet = [1, 2, 3, 4, 5]
#     everySubset(oriSet)
#     print(s_s)

# import copy
#
# s_s = []
# def everySubset(oriSet, subSet=[], last=0):
#     print(subSet)
#     s_s.append(subSet)
#     if last == len(oriSet) + 1:
#         return
#
#     for i in range(last, len(oriSet)):
#         next_subSet = copy.deepcopy(subSet)
#         next_subSet.append(oriSet[i])
#         everySubset(oriSet, next_subSet, i + 1)
#
#
# if __name__ == '__main__':
#     oriSet = [1, 2, 3, 4, 5]
#     everySubset(oriSet)
#     print(s_s)

pick = []
# for i in range(5):
#     for j in range(i+1, 5):
#         for k in range(j+1, 5):
#             pick.append([i,j,k])

def Combo(N,K,s):
    if K == 2:
        pick.append[]
        return
    for i in range(s, 5):
