T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    vote = [0]*N
    for i in range(M):
        for j in range(N):
            if B[i]>=A[j]:
                vote[j] += 1
                break
    print("#{} {}".format(t,vote.index(max(vote))+1))