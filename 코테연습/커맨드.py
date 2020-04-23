def solution(directory, command):
    for c in command:
        coman = c.split()
        if len(coman)<3:
            co, point = coman
        if co == "mkdir":
            slash = point.count('/')
            cnt = 0
            upper_p=''
            file_name = ''
            for s in point:
                if s == '/':
                    cnt += 1
                if cnt<slash:
                    upper_p += s
                else:
                    file_name += s
            if slash == 1:
                directory.append(point)
            else:
                for i in range(1,len(directory)):
                    if upper_p == directory[i]:
                        directory.append(directory[i]+file_name)
                        continue
    return directory

print(solution([
"/",
"/hello",
"/hello/tmp",
"/root",
"/root/abcd",
"/root/abcd/etc",
"/root/abcd/hello"
],[
"mkdir /root/tmp",
"cp /hello /root/tmp",
"rm /hello"
]))