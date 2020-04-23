# n = int(input())
# def stack_number():
#     stack = []
#     ans = [0]*(2*n)
#     print_n=[int(input()) for _ in range(n)]
#     idx = 1
#     print_cnt = 0
#     idx_ans = 0
#     for i in range(n):
#         num = print_n[i]
#         while stack and print_cnt<i and print_n[print_cnt]<num:
#             ans[idx_ans]='-'
#             idx_ans += 1
#             if stack.pop() != print_n[print_cnt]:
#                 print('NO')
#                 return
#             print_cnt += 1
#         if num in stack:continue
#         for k in range(idx,num+1):
#             stack.append(k)
#             ans[idx_ans]='+'
#             idx_ans += 1
#         idx = num+1
#     for j in range(len(stack)-1,-1,-1):
#         if stack[j] != print_n[print_cnt]:
#             print('NO')
#             return
#         ans[idx_ans]='-'
#         idx_ans+=1
#         print_cnt+=1
#     print('\n'.join(ans))
#
# stack_number()

n = int(input())
arr = [int(input()) for _ in range(n)]
ans = [0]*(2*n)
stack = []
idx = 0
idx_ans = 0
for i in range(n):
    stack.append(i+1)
    ans[idx_ans] = '+'
    idx_ans += 1
    while stack and idx<n and arr[idx]==stack[-1]:
        ans[idx_ans] = '-'
        stack.pop()
        idx_ans += 1
        idx+=1
if ans.count(0):print('NO')
else:
    print('\n'.join(ans))