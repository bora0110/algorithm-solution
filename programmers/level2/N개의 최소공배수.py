from math import gcd


# 유클리드 호제법
def GCD(x, y):
    while (y):
        x, y = y, x % y
    return x


def solution(arr):
    answer = arr[0]
    for num in arr:
        answer = answer * num // GCD(answer, num)

    return answer


arr = [2, 6, 8, 14]
print(solution(arr))
