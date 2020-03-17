# T = int(input())
# # for t in range(1,T+1):
# #     A, B = input().split()
# #     cnt = A.count(B)
# #     print("#{} {}".format(t,len(A)-(len(B)-1)*cnt))

for tc in range(int(input())):
    A ,B = input().split()
    cnt = 0
    n = 0
    long = len(A)
    reset = ''
    for i in range(len(B)):
        reset += '0'
    for i in range(n,len(A)-len(B)+1):
        if A[i:i+len(B)] == B:
            cnt += 1
            A = reset+A[i+len(B):]
    print('#{} {}'.format(tc+1,long - cnt * (len(B)-1)))
