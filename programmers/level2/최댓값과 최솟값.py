def solution(s):
    s = list(map(int, s.split()))

    # return str(min(s)) + ' ' + str(max(s))
    return f'{min(s)} {max(s)}'


ss = '-1 -2 -3 -4 4'
print(solution(ss))
