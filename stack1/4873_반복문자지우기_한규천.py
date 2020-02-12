T = int(input())
for t in range(1, T+1):
    words = input()
    stack = []
    for w in words:
        if len(stack) != 0:
            if stack[-1] != w:
                stack.append(w)
            elif len(stack) != 0:
                stack.pop(-1)
        else:
            stack.append(w)
    print("#{} {}".format(t, len(stack)))