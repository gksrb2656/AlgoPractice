# for i in range(5):
#     for j in range(i+1, 5):
#         for k in range(j+1, 5):
#             print(i, j, k)

arr = 'ABCDE'
print(list(arr))
N = len(arr)
R=3
pick=[0]*R
def comb(k,s):#k-depth s - 반복의 시작위치
    if k == R:
        for i in pick:
            print(arr[i], end = ' ')
        print()
    else:
        for i in range(s,N):
            pick[k] =i
            comb(k+1,i+1)
comb(0,0)

# def Comb(k, s):
