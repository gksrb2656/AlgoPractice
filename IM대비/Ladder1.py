dr = [0, 0, 1]
dc = [1, -1, 0]
for t in range(1,11):
    T=int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    point = ''
    for i in range(100):
        visit = []
        if ladder[0][i] == 1:
            r, c = 0, i
            visit.append([r,c])
            while r < 99:
                r, c = visit[-1]
                for k in range(3):
                    nr = r+dr[k]
                    nc = c+dc[k]
                    if nr>99 or nc>99 or nr<0 or nc<0 or [nr,nc] in visit:
                        continue
                    if ladder[nr][nc] == 1:
                        visit.append([nr,nc])
                        break
                    elif ladder[nr][nc] == 2:
                        visit.append([nr, nc])
                        point = i
                        print("#{} {}".format(t, point))
                        break
        if point != '':
            break

# for t in range(1,11):
#     T = int(input())
#     li = [list(map(int, input().split())) for _ in range(100)]
#     point = 0
#     for j in range(100):
#         if li[0][j] == 1:
#             r = 0
#             c = j
#             while r < 99:
#                 if li[r+1][c] == 1:
#                     r += 1
#                     if c < 99 and li[r][c+1]==1:
#                         while c < 99 and li[r][c+1]:
#                             c += 1
#                         continue
#                     elif c > 0 and li[r][c-1]==1:
#                         while c > 0 and li[r][c-1]:
#                             c -= 1
#                 elif li[r+1][c] == 2:
#                     point = j
#                     break
#     print('#{} {}'.format(t, point))
