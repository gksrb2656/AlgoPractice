def solution(snapshots, transactions):
    ID = [0]*(100000)
    for i in range(len(transactions)):
        flag = 0
        for j in range(len(snapshots)):
            if transactions[i][2] == snapshots[j][0]:
                flag = 1
                if not ID[int(transactions[i][0])]:
                    if transactions[i][1]=="WITHDRAW":
                        snapshots[j][1] = str(int(snapshots[j][1])-int(transactions[i][3]))
                        ID[int(transactions[i][0])] = 1
                    else:
                        snapshots[j][1] = str(int(snapshots[j][1])+int(transactions[i][3]))
                        ID[int(transactions[i][0])] = 1
        if not flag:
            snapshots.append([transactions[i][2],transactions[i][3]])
    return sorted(snapshots)

solution([
  ["ACCOUNT1", "100"],
  ["ACCOUNT2", "150"]
],[
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"],
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["4", "SAVE", "ACCOUNT3", "500"],
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
])