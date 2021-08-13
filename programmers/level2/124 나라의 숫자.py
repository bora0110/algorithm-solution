def solution(n):
    answer = ''
    if n <= 3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return solution(q) + '124'[r]

    return answer


n = 1
print(solution(n))

n = 3
print(solution(n))

n = 7
print(solution(n))

n = 10
print(solution(n))

