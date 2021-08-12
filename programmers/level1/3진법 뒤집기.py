def solution(n):
    answer = 0

    # 숫자 n을 q진법으로 변환
    def sol(n, q):
        rev_base = ''

        while n > 0:
            n, mod = divmod(n, q)
            rev_base += str(mod)
        return rev_base[::-1]

    num = sol(n, 3)
    # print(num)
    num = num[::-1]  # 뒤집기
    # print(num)
    answer = int(num, 3)
    return answer

n = 45
print(solution(n))