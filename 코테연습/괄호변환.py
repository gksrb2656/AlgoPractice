global answer
def check(words):
    on = 0
    off = 0
    if not words:
        return ''
    for w in range(len(words)):
        if words[w] == '(':
            on += 1
        else:
            off += 1
        if not on - off:
            return right(words[:w+1],words[w+1:])

def right(words_u, words_v):
    global answer
    stack = []
    for w in words_u:
        if not stack:
            stack.append(w)
        elif stack[-1] =='(' and w==')':
            stack.pop()
        else:
            stack.append(w)
    if not stack:
        return(words_u+check(words_v))
    else:
        return('('+check(words_v)+')'+reverse(words_u))

def reverse(word):
    rev = ''
    for w in word[1:-1]:
        if w == '(':
            rev += ')'
        else:
            rev += '('
    return rev

def solution(p):
    return check(p)

print(solution('()))((()'))