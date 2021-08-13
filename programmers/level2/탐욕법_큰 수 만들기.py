def solution(number, k):
    answer = ''

    stack = [number[0]]

    for num in number[1:]:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()

        stack.append(num)

    if k != 0:
        stack = stack[:-k]

    answer = ''.join(stack)

    return answer


nn = "1924"
kk = 2
print(solution(nn, kk))