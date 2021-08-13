import itertools
import math


def is_prime_number(num):
    if num == 0 or num == 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0

    lst = list(numbers)
    new_set_lst = []

    for i in range(1, len(numbers)+1):
        for s in itertools.permutations(lst, i):
                new_set_lst.append(int("".join(s)))

    new_set_lst = list(set(new_set_lst))
    print(new_set_lst)
    for num in new_set_lst:
        if is_prime_number(num):
            answer += 1

    return answer


numbers = '011'
print(solution(numbers))
