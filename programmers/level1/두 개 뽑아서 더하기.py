import itertools


def solution(numbers):
    answer = []

    for a in itertools.combinations(numbers, 2):
        answer.append(sum(a))

    answer = list(set(answer))
    answer.sort()
    return answer


numbers = [2, 1, 3, 4, 1]
print(solution(numbers))
