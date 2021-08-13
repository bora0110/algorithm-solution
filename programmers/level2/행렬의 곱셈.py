def solution(arr1, arr2):
    arr1_r = len(arr1)
    arr1_c = len(arr1[0])

    arr2_c = len(arr2[0])
    answer = [[0] * arr2_c for _ in range(arr1_r)]

    for i in range(arr1_r):
        for j in range(arr2_c):
            number = 0
            for a in range(len(arr2)):
                number += arr1[i][a] * arr2[a][j]
            answer[i][j] = number

    return answer


aa = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
bb = [[5, 4], [2, 4], [3, 1]]

print(solution(aa, bb))
