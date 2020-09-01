def solution(s):
    Min = len(s)
    for i in range(1,len(s)//2+1):
        now = s[:i]
        flag = 1
        cnt = len(s)
        k = 1
        for j in range(1,len(s)//i):
            if now == s[i*j:i*(j+1)]:
                if flag>1:
                    flag += 1
                    if flag//(10*k):
                        k *= 10
                        cnt += 1
                    cnt -= i
                else:
                    flag = 2
                    cnt -= (i-1)
            else:
                now = s[i*j:i*(j+1)]
                flag = 1
                k = 1
        Min = min(cnt,Min)
    answer = Min
    return answer

print(solution("a"*10+'b'*10))

# def compress(text, tok_len):
#     words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
#     res = []
#     cur_word = words[0]
#     cur_cnt = 1
#     for a, b in zip(words, words[1:] + ['']):
#         if a == b:
#             cur_cnt += 1
#         else:
#             res.append([cur_word, cur_cnt])
#             cur_word = b
#             cur_cnt = 1
#     return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)
#
# def solution(text):
#     return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

print(solution("aabbababcdcd"))