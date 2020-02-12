T = int(input())
for t in range(1, T+1):
    case = input()
    stack = list()
    result = 1
    for w in case:
        if w == '{' or w =='(':
            stack.append(w)
        elif w == ')':
            if len(stack) == 0:
                result = 0
                break
            elif stack[-1] == '(':
                    stack.pop(-1)
            elif stack[-1] == '{':
                result = 0
                break
        elif w == '}':
            if len(stack) == 0:
                result = 0
                break
            elif stack[-1] == '{':
                stack.pop(-1)
            elif stack[-1] == '(':
                result = 0
                break
    if result:
        if len(stack) == 0:
            print("#{} 1".format(t))
        else:
            print("#{} 0".format(t))
    else:
        print("#{} 0".format(t))
