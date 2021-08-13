from collections import deque


def solution(n,a,b):
    answer = 0

    q = [i for i in range(1, n+1)]
    q = deque(q)
    print(q)

    while q:
        x = q.popleft()
        y = q.popleft()

        if [x,y] == [a,b] or [x,y] == [b,a]:
            answer += 1
            break

        if a in [x, y]:
            answer += 1
            q.append(a)
        elif b in [x, y]:
            q.append(b)
        else:
            q.append(x)

    return answer

n = 8
a = 4
b = 7
print(solution(n, a, b))