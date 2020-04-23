def solution(stones, k):
    MAX = max(stones)
    ans = MAX
    def binary(st, ed, k):
        nonlocal ans
        if st>=ed:return
        mid = (st+ed)//2
        if mid == ans:return
        cnt = 0
        for i in stones:
            if i<=mid:
                cnt += 1
                if cnt == k:
                    if ans>cnt:
                        ans = mid
                        binary(st, mid, k)
                    return
            else:
                cnt = 0

        binary(mid+1, ed, k)
    if k!=len(stones):
        binary(1, MAX+1, k)
    return ans