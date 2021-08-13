def solution(s):
    answer = ''

    i = 0
    flag = True

    s = s.lower()
    while i < len(s):
        if s[i] == ' ':
            i += 1
            flag = True
            continue
        elif flag:
            flag = False
            if s[i].isalpha():
                s = s[:i] + s[i].upper() + s[i+1:]
        i += 1

    answer = s

    return answer

def solution_other(s):
    answer = s
    return s.lower().title()

s = " 3peo  ple unFollowed me"
print(solution(s))
print(solution_other(s)) # 첫 문자가 숫자면 안됨