def solution(a, b):
    i = min(a, b)
    j = max(a, b)
    return sum([i for i in range(i, j + 1)])


def solution_new(a, b):
    if a > b: a, b = b, a
    return sum(range(a, b + 1))


a = 3
b = 5
print(solution(a, b))
print(solution_new(a, b))