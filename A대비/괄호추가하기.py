def calculation(e,a,b):
    if e =='+':
        return a+b
    elif e == '-':
        return a-b
    else:
        return a*b

def comb(k,n,depth,nums):
    global c_s_copy
    global MAX
    nums_copy = nums[:]
    if k == depth:
        for c in c_s_idx:
            if len(nums_copy)>1:
                nums_copy = [calculation(c_s[c],nums_copy[0],nums_copy[1])] + nums_copy[2:]
        MAX = max(MAX,nums_copy[0])
        return

    for i in range(n,K):
        if len(nums_copy)-1 != i-depth+1:
            nums_copy = nums_copy[:i-depth]+[calculation(c_s[i], nums_copy[i-depth], nums_copy[i-depth+1])] + nums_copy[i-depth+2:]
        else:
            nums_copy = nums_copy[:i - depth] + [calculation(c_s[i], nums_copy[i - depth], nums_copy[i - depth + 1])]
        c_s_idx.remove(i)
        comb(k,i+2,depth+1,nums_copy)
        c_s_idx.append(i)
        c_s_idx.sort()
        nums_copy = nums[:]

N = int(input())
cal = list(input())
K = N//2
nums = [0]*(K+1)
c_s =[0]*(K)
for i in range(N):
    if i%2:
        c_s[i//2] = cal[i]
    else:
        nums[i//2] = int(cal[i])

MAX = -2**31
if len(cal) == 1:
    print(cal[0])
else:
    for k in range(1,len(c_s)+1):
        c_s_idx = [i for i in range(K)]
        comb(k,0,0,nums)
    print(MAX)
