def solution(arr):
    answer = [0, 0]
    n = len(arr)

    def divide(r, c, n):
        num = arr[r][c]

        for i in range(r, r + n):
            for j in range(c, c + n):
                if num != arr[i][j]:
                    divide(r, c, n // 2)
                    divide(r + n // 2, c, n // 2)
                    divide(r, c + n // 2, n // 2)
                    divide(r + n // 2, c + n // 2, n // 2)
                    return
        answer[num] += 1

    divide(0, 0, n)
    return answer


arr = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]
print(solution(arr))
