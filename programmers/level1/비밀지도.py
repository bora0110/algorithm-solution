def solution(n, arr1, arr2):
    answer = []
    for decimal1, decimal2 in zip(arr1, arr2):
        binary12 = str(bin(decimal1 | decimal2))[2:]

        binary12 = binary12.rjust(n, '0')  # n 길이만큼 오른쪽에 0 채우기
        binary12 = binary12.replace('1', '#')
        binary12 = binary12.replace('0', ' ')
        answer.append(binary12)
    return answer


aa = 5
bb = [9, 20, 28, 18, 11]
cc = [30, 1, 21, 17, 28]
print(solution(aa, bb, cc))
