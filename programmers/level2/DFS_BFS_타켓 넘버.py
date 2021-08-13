import collections

answer = 0


def solution(numbers, target):
    total = 0
    global answer

    def dfs(index, total):
        global answer
        if len(numbers) == index:
            if total == target:
                answer += 1
            return

        dfs(index + 1, total + numbers[index])
        dfs(index + 1, total - numbers[index])

    dfs(0, 0)

    return answer


nums = [1, 1, 1, 1, 1]
target = 3
print(solution(nums, target))
