def solution(msg):
    answer = []
    dic = {}
    for i,al in zip(range(1, 27), range(65, 91)):
        dic[chr(al)] = i

    print(dic)

    i = 0
    j = 1

    while True:
        if msg[i:j] in dic:
            j += 1
            if j >= len(msg) + 1:
                answer.append(dic[msg[i:j]])
                break

        else:
            dic[msg[i:j]] = len(dic) + 1
            answer.append(dic[msg[i:j-1]])
            i += len(msg[i:j-1])
            j = i + 1
    return answer


aa = "KAKAO"
print(solution(aa))