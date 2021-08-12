import math
import itertools


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    for n in itertools.combinations(nums, 3):
        if is_prime_number(sum(n)):
            answer += 1

    return answer


nums = [1, 2, 7, 6, 4]
print(solution(nums))
