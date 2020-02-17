T = int(input())
for t in range(1, T+1):
    stack = []
    li = input().split()
    for i in li:
        if i.isdigit():
            stack.append(int(i))
        elif i in '+-*/':
            if len(stack) >=2:
                if i == '+':
                    d1 = stack.pop()
                    stack[-1] = d1+stack[-1]
                if i == '-':
                    d1 = stack.pop()
                    stack[-1] = stack[-1]-d1
                if i == '*':
                    d1 = stack.pop()
                    stack[-1] = stack[-1]*d1
                if i == '/':
                    d1 = stack.pop()
                    stack[-1] = stack[-1]//d1
            else:
                print('#{} error'.format(t))
                break
        elif i == '.' and len(stack) == 1:
            print('#{} {}'.format(t, stack.pop()))
        else:
            print('#{} error'.format(t))