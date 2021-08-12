def solution(s):
    answer = ''
    if len(s) % 2 == 0:  # 짝수
        answer = s[int(len(s)/2)-1:int(len(s)/2)+1]
    else:
        answer = s[int(len(s)/2)]
    return answer

print(solution("abcde"))