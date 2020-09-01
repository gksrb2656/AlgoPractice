def turn(arr, M):
    temp = [[0]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            temp[j][M-i-1] = arr[i][j]
    return temp

def padding(lock,N,M):
    for i in range(M-1):
        lock.insert(0,[2]*(N))
        lock.append([2]*(N))
    for i in range(len(lock)):
        lock[i] = [2]*(M-1) + lock[i] + [2]*(M-1)

def check(st_x,st_y,lock,key,z_cnt,M):
    for i in range(M):
        for j in range(M):
            if lock[st_x+i][st_y+j] == 0:
                if key[i][j] == 1:
                    z_cnt -= 1
            elif lock[st_x+i][st_y+j] == 1:
                if key[i][j] == 1:
                    return 0
    if not z_cnt:
        return 1

def solution(key, lock):
    M = len(key)
    N = len(lock)
    z_cnt = 0
    for l in lock:
        z_cnt += l.count(0)
    padding(lock,N,M)
    for _ in range(4):
        for i in range(len(lock)-M+1):
            for j in range(len(lock)-M+1):
                if check(i,j,lock,key,z_cnt,M):
                    return True
        key = turn(key,M)
    return False

solution(	[[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])