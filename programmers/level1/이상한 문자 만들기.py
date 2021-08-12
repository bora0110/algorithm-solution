def solution(s):
    answer = ''
    lst = s.split(" ")
    for str in lst:
        for i, w in enumerate(list(str)):
            if i % 2 == 0:
                answer += w.upper()
            else:
                answer += w.lower()

        answer += " "
    return answer[:-1]


def solution_new(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))


aa = "try hello world"
print(solution(aa))
