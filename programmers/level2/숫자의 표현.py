def solution(n):
    print([i for i in range(1, n + 1, 2) if n % i is 0])
    return len([i for i in range(1, n + 1, 2) if n % i is 0])


print(solution(15))
