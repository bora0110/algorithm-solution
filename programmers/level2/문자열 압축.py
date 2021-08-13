def solution(s):
    if len(s) == 1: return 1

    answer = 1001
    half_size = len(s) // 2 + 1
    for size in range(1, half_size):
        base = s[:size]
        print(base)

        result = base  # 첫번째 값을 결과에 넣는다
        count = 0

        for st in range(0, len(s) + 1, size):

            if s[st:st + size] == base:
                count += 1
            else:
                base = s[st:st + size]
                if count == 1:
                    result += s[st:st + size]
                else:
                    result += str(count) + s[st:st + size]
                count = 1

        answer = min(answer, len(result))
    return answer


s = "ababcdcdababcdcd"
print(solution(s))
