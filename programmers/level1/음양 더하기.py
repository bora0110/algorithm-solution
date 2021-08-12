def solution(absolutes, signs):
    answer = 0

    for a, b in zip(absolutes, signs):
        if b:
            answer += a
        else:
            answer -= a
    return answer


absolutes = [4, 7, 12]
signs = [True, False, True]
print(solution(absolutes, signs))
