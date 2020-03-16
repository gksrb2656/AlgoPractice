T = int(input())
for t in range(1,T+1):
    A = input()
    B = input()
    cnt = A.count(B)
    print(cnt)
    print(len(A)-len(B)*(cnt-1))