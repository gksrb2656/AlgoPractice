def back(cal):
    stack = []
    li = []
    for i in cal:
        if i.isdigit():
            li.append(i)
        elif i in '+-*/':
            if i =='+':
                if stack:
                    while stack[-1] == '*' or stack[-1] == '/':
                        li.append(stack.pop())
                stack.append(i)
            elif i == '-':
                if stack:
                    while stack[-1] == '*' or stack[-1] == '/':
                        li.append(stack.pop())
                stack.append(i)
            else:
                stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                li.append(stack.pop())
            stack.pop()
    while stack:
        if stack[-1] == '(':
            pass
        else:
            li.append(stack.pop())
    return li

for t in range(1, 11):
    N = int(input())
    cal = input()
    stack2 = []
    li = back(cal)
    for i in li:
        if i.isdigit():
            stack2.append(int(i))
        elif i in '+-*/':
            if len(stack2) >=2:
                if i == '+':
                    d1 = stack2.pop()
                    stack2[-1] = stack2[-1]+d1
                if i == '-':
                    d1 = stack2.pop()
                    stack2[-1] = stack2[-1]-d1
                if i == '*':
                    d1 = stack2.pop()
                    stack2[-1] = stack2[-1]*d1
                if i == '/':
                    d1 = stack2.pop()
                    stack2[-1] = stack2[-1]//d1
    print('#{} {}'.format(t, stack2.pop()))
