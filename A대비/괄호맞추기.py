# data = list(input())
# for d in range(len(data)):
#     if data[d] == '-':
#         data[d] = data[d-1]
# for d in range(len(data)-1,-1,-1):
#     if data[d] =='+':
#         data[d] = data[d+1]
#
# s=m=l=0
# def inspection(w):
#     global s, m, l
#     if w == '(':
#         s += 1
#     if w == ')':
#         if s == 0:
#             print('False')
#             return 0
#         else:
#             s -= 1
#     if w == '{':
#         m += 1
#     if w == '}':
#         if m == 0:
#             print('False')
#             return 0
#         else:
#             m -= 1
#     if w == '[':
#         l += 1
#     if w == ']':
#         if l == 0:
#             print('False')
#             return 0
#         else:
#             l -= 1
#     return 1
#
# flag = 1
# for d in range(len(data)):
#     if not inspection(data[d]):
#         flag = 0
#         break
#
# if flag and s+m+l==0:
#     print('True')
# elif flag and s+m+l != 0:
#     print('False')

data = list(input())
minus = []
plus = []
for d in range(len(data)):
    if data[d] == '-':
        for dd in range(d-1,-1,-1):
            if data[dd] != '+' and data[dd]!='-':
                minus.append(data[dd])
                break
for d in range(len(data)-1,-1,-1):
    if data[d] =='+':
        for dd in range(d+1,len(data)):
            if data[dd] != '-' and data[dd]!='+':
                plus.append(data[dd])
                break
for d in range(len(data)-1,-1,-1):
    if data[d] == '-':
        data[d] = minus.pop()

for d in range(len(data)):
    if data[d] =='+':
        data[d] = plus.pop()

stack = []

dir = {'(':')','{':'}','[':']'}
for d in data:
    if not stack:
        stack.append(d)
    else:
        if dir.get(stack[-1]):
            if dir[stack[-1]] == d:
                stack.pop()
            else:
                stack.append(d)
        else:
            stack.append(d)
if not stack:
    print('True')
else:
    print('False')
