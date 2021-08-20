def solution(n, s):
    answer = []
    if n > s:
        return [-1]

    [p, r] = divmod(s, n)
    answer = [p]*n

    for i in range(r):
        answer[i] += 1

    answer.sort()
    return answer