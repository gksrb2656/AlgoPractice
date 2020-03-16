T = int(input())
for t in range(1,T+1):
    arr = list(input())
    rzr = 0
    p_s = []
    ans = 0
    for i in range(len(arr)):
        if arr[i] == '(' and arr[i+1] == ')':
            if p_s:
                for j in range(len(p_s)):
                    p_s[j] += 1
        elif arr[i] == '(':
            p_s += [0]
        elif arr[i] == ')' and arr[i-1] != '(':
            if p_s:
                ans += p_s.pop()+1
    print("#{} {}".format(t,ans))