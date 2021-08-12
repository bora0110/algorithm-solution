def solution(nums):
    answer = 0

    cnt = int(len(nums) / 2)
    lst = set(nums)

    if len(lst) >= cnt:
        answer = cnt
    else:
        answer = len(lst)

    return answer


nums = [3, 1, 2, 3]
print(solution(nums))
