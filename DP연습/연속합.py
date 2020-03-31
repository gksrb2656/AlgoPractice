N = int(input())
nums = list(map(int, input().split()))
S = nums[0]
Max = S
for i in range(1,N):
    if S+nums[i]<0 or S<0:
        S = nums[i]
    else:
        S += nums[i]
    if S>Max:
        Max = S
print(Max)