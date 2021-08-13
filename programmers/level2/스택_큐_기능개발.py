def solution(progresses, speeds):
    answer = []
    day = []
    temp = 0
    for p, s in zip(progresses, speeds):
        temp = (100 - p) // s
        if (100 - p) % s > 0: temp = temp + 1
        day.append(temp)

    print(day)

    max = 0
    for i, d in enumerate(day):
        if i == 0:
            max = d
            answer.append(1)
        elif d <= max:
            answer[-1] += 1
        elif d > max:
            max = d
            answer.append(1)
    return answer


p = [93, 30, 55]
s = [1, 30, 5]

print(solution(p, s))
