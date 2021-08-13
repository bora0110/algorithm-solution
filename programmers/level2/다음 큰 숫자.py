def solution(n):
    answer = 0

    num = bin(n)[2:].count('1')

    while True:
        n += 1
        if bin(n)[2:].count('1') == num:
            answer = n
            break

    return answer


nn = 15
print(solution(nn))