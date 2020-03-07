T = int(input())
for tc in range(1, T+1):
    d = input()
    data = map(int, input().split())
    a=1
    for i in data:
        print(i,bin(a), bin(a<<i))
        a |= a<<i
        print(a)
    print('#%i'%tc,bin(a).count('1'))



# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     score = [0]
#     set_score = set(score)
#     for i in scores:
#         for j in list(set_score):
#             set_score.add(i+j)
#
#     print("#{} {}".format(t,len(set_score)))


# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     Max = sum(scores)
#     p_s = [0]
#     visit = [0]*(Max+1)
#     for i in scores:
#         for j in range(len(p_s)):
#             if visit[p_s[j]+i]:continue
#             p_s += [p_s[j]+i]
#             visit[p_s[j] + i] = 1
#
#     print("#{} {}".format(t,len(p_s)))

# T = int(input())
# for t in range(1,T+1):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     Max = sum(scores)
#     visit = [0]*(Max+1)
#     visit[0] = 1
#     cnt = 0
#     for i in scores:
#         for j in range(Max,-1,-1):
#             if visit[j]:
#                 visit[j+i] = 1
#     for k in range(Max+1):
#         if visit[k]:
#             cnt +=1
#     print("#{} {}".format(t,cnt))