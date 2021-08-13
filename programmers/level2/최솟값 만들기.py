def solution(A, B):
    answer = 0

    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer
#   return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))


aa = [1, 4, 2]
bb = [5, 4, 4]
print(solution(aa, bb))
