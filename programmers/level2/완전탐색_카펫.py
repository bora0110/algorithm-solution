def solution(brown, yellow):
    answer = []
    all_cnt = brown + yellow

    for i in range(brown, 2, -1):
        if all_cnt % i == 0:
            x = all_cnt // i
            if yellow == (i - 2) * (x - 2):
                return [i, x]

    return answer


b = 10
y = 2
print(solution(b, y))
