def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        # 제곱수는 약수의 갯수가 홀수
        if int(i ** 0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i
    return answer


def solution_old(left, right):
    answer = 0
    for i in range(left, right + 1):
        now_cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                now_cnt += 1
        if now_cnt % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer


left = 13
right = 17
print(solution(left, right))
print(solution_old(left, right))
