def solution(s):
    answer = []
    zero = 0
    cycle = 0

    if s == '1':
        return [0, 0]

    while s != '1':
        zero += s.count('0')
        s = s.replace('0', '')
        if s == '1': break
        s = bin(len(s))[2:]
        cycle += 1

    return [cycle+1, zero]


aa = "110010101001"
print(solution(aa))