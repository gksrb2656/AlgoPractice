def cal(pay_sum,n):
    global salary
    if n>N:
        if pay_sum>salary:
            salary = pay_sum
        return
    for d in range(n,N+1):
        if d + c_s[d] - 1<=N:
            pay_sum+=pay[d]
            cal(pay_sum,d+c_s[d])
            pay_sum -= pay[d]
        elif pay_sum>salary:
            salary = pay_sum

N = int(input())
c_s = [0]*(N+1)
pay = [0]*(N+1)
salary = 0
for i in range(1,N+1):
    day, p = map(int, input().split())
    c_s[i] = day
    pay[i] = p

cal(0,1)
print(salary)


# def resign(d,m,money):
#     global MAX
#     for i in range(d,m):
#         if d>N-1:
#             if money>MAX:
#                 MAX=money
#             return
#         if i+day[i]-1<=N-1:
#             money+=income[i]
#             resign(i+day[i],m,money)
# N=int(input())
# day=[]
# income=[]
# MAX=0
# for i in range(N):
#     T,P=map(int,input().split())
#     day.append(T)
#     income.append(P)
# resign(0,N,0)
# print(MAX)