def solution(record):
    answer = []
    ID_nick = {}
    for r in range(len(record)):
        data = record[r].split()
        if data[0] != 'Leave':
            ID_nick[data[1]] = data[2]
    for r in record:
        data = r.split()
        if data[0] == 'Enter':
            answer.append(ID_nick[data[1]]+'님이 들어왔습니다.')
        elif data[0] == 'Leave':
            answer.append(ID_nick[data[1]]+'님이 나갔습니다.')
    return answer

solution(	["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])