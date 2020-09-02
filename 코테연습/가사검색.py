# from collections import defaultdict
# def solution(words, queries):
#     answer = [0] * len(queries)
#     memo_q = dict()
#     words_len = defaultdict(list)
#     idx_q = -1
#     for w in range(len(words)):
#         words_len[len(words[w])].append(words[w])
#     for q in queries:
#         idx_q += 1
#         if q in memo_q:
#             answer[idx_q] = memo_q[q]
#             continue
#         if q[0] == '?' and q[-1] == '?':
#             answer[idx_q] = len(words_len[len(q)])
#             memo_q[q] = answer[idx_q]
#             continue
#         st = -1
#         ed = len(q)
#         for i in range(len(q)):
#             if st==-1 and q[i] != '?':
#                 st = i
#             if -1<st<i and q[i] == '?':
#                 ed = i
#                 break
#         for w in words_len[len(q)]:
#             if q[st:ed] == w[st:ed]:
#                 answer[idx_q] += 1
#         memo_q[q] = answer[idx_q]
#     return answer
#
def solution(words, queries):
    trie_by_length = [({}, {}) for _ in range(10001)]
    for word in words:
        length = len(word)
        t = trie_by_length[length][0]
        for c in word:
            t['count'] = t.get('count', 0) + 1
            t.setdefault(c, {})
            t = t[c]
        t = trie_by_length[length][1]
        for c in word[::-1]:
            t['count'] = t.get('count', 0) + 1
            t.setdefault(c, {})
            t = t[c]
    ans = []
    for query in queries:
        length = len(query)
        if query[0] == '?':
            t = trie_by_length[length][1]
            query = query[::-1]
        else:
            t = trie_by_length[length][0]
        for c in query:
            if c == '?':
                ans.append(t.get('count', 0))
                break
            if c not in t:
                ans.append(0)
                break
            t = t[c]
    return ans


solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])