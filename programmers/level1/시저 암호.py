def solution(s, n):
    answer = ''
    dic1 = {e: chr(e + 64) for e in range(1, 27)}
    dic2 = {chr(e + 64): e for e in range(1, 27)}
    # print(dic1)
    # print(dic2)

    for w in s:
        temp_w = w
        is_upper = True  # 대문자
        if w == " ":
            answer += " "
            continue
        if not w.isupper():
            is_upper = False  # 소문자
            temp_w = w.upper()
        idx = dic2[temp_w]

        if (idx + n) > 26:
            idx = (idx + n) % 26
        else:
            idx = idx + n

        if is_upper:
            answer += dic1[idx]
        else:
            answer += dic1[idx].lower()
    return answer


def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return "".join(s)


aa = "a"
bb = 25
print(solution(aa, bb))
