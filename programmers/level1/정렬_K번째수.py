def solution(array, commands):
    answer = []

    for cmd in commands:
        i, j, k = cmd[0], cmd[1], cmd[2]
        i = i - 1
        # print(i, j, k)
        answer.append(sorted(array[i:j])[k - 1])
    return answer


arr = [1, 5, 2, 6, 3, 7, 4]
print(solution(arr))
