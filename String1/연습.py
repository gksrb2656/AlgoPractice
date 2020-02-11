# print('안녕하세요')
#
# print("I'm iron man")
#
# print('''"임동규 선수를 트레이드 하겠습니다."라고 백승수 단장이 말했다.''')
#
# print('나는\nIM을\n딸 수 있다.')
#
# print('허리', '피라우')
#
# print('껄'*3)
# def check(pw):
#     cnt_n = 0
#     cnt_a = 0
#     pw = ''
#     for i in range(len(pw)):
#         if pw[i].isalpha():
#             cnt_a +=1
#         if pw[i].isdigit():
#             cnt_n += 1
#
#     if cnt_n >= 3 and cnt_a>=4:
#         return '유효'
#     else:
#         return '비번 다시 쓰거라'
#
# while 1:
#     password = input('비밀번호를 입력해주세요.(종료)라고 입력시 종료')
#     if password =='종료':
#         break
#     else:
#         print(check(password))

# for i in range(4):
#     n = 0
#     s = 0
#     password = input()
#     for j in password:
#         if j.isalpha():
#             s+=1
#         if j.isnumeric():
#             n+=1
#     if n <3 or s < 4:
#         print('비밀번호는 숫자가 3개이상 문자가 4개이상이어야 올바른 비밀번호이다.')

# words = '삼성청년소프트웨어아카데미'
# for i in range(len(words),0,-1):
#     print(words[i-1], end='')
# print()
#
# words_l = list(words)
# words_l.reverse()
# print(''.join(words_l))
#
# words_l.reverse()
# for i in range(len(words_l)//2):
#     words_l[i], words_l[len(words_l)-i-1] = words_l[len(words_l)-i-1], words_l[i]
# print(''.join(words_l))
#
# words2 = words[::-1]
# print(words2)
#
# words3 = reversed(words)
# print(''.join(words3))

# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]
# print(a==b)
# print(a==c) # == 연산자는 값을 비교!
# print(a is b)
# print(a is c) # is 연산자는 주소를 비교!

# def atoi(s):
#     n = 0
#     for i in range(len(s)):
#         n += (ord(s[i])-48)*(10**(len(s)-i-1))
#     return n
#
# a=atoi('11119')
# print(a)
#
# def itoa(n):
#     s = ''
#     while 1:
#         i = n%10
#         n = n//10
#         s = chr(i%10+48) + s
#         if n == 0:
#             break
#     return s
# b=itoa(11117)
# print(b)

# def pattern_matching(t, p):
#     cnt1 = 0
#     for i in range(len(t)-len(p)+1):
#         cnt = 0
#         for j in range(i, len(p)+i):
#             cnt1 += 1
#             if p[j-i] != t[j]:
#                 cnt = 0
#                 break
#             else:
#                 cnt += 1
#             if cnt == len(p):
#                 idx = i
#                 print('검색성공')
#                 print('start_idx:',idx)
#     print(cnt1)
li = [1,2,3,4,5,6,7,8]
print(li[7:4:-1])

# pattern_matching('A pattern matching algorithm', 'rithm')

# def boyer(t, p):

