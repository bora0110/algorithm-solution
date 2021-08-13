def solution_old(s):
    # 시간 초과
    answer = True

    while True:
        if '()' in s:
            s = s.replace('()', '')
        else:
            break

    if s == '':
        return True
    else:
        return False


def solution_new(s):
    answer = True
    stack = []

    for str in s:
        if str == '(':
            stack.append(str)
        else:
            if not stack:
                return False
            stack.pop()

    if stack:
        return False
    else:
        return True


def solution_good(s):
    # 함수를 완성하세요
    x = 0
    for w in s:
        if x < 0:
            break
        x = x + 1 if w == "(" else x - 1 if w == ")" else x
    return x == 0


ss = ")()("
print(solution_old(ss))
print(solution_new(ss))
print(solution_good(ss))
