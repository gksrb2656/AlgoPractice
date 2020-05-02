for t in range(1, int(input())+1):
    N, hexa = map(str, input().split())

    ans =[]
    for val in hexa:
        val = int(val, 16)
        for i in range(3,-1,-1):
            ans.append(1 if val & 2**i else 0)

print(ans)