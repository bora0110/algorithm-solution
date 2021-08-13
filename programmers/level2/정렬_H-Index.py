def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    print(citations)

    a = list(map(min, enumerate(citations, start=1)))
    print(a)
    answer = max(a)
    return answer


aa = [3, 0, 6, 1, 5]
print(solution(aa))

