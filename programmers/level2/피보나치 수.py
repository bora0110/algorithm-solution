import sys

sys.setrecursionlimit(10 ** 6)

# 반복적 동적 계획법
def solution_old(n):
    lst = [0,1]

    for i in range(2, n + 1):
        lst.append(lst[i - 1] + lst[i - 2])

    return lst[-1] % 1234567

def solution_new(n):
    f_list = [0,1]
    for i in range(2,n+1):
        f_list.append((f_list[i-2]%1234567+f_list[i-1]%1234567)%1234567)
    return f_list[-1]

# 재귀적 동적 계획법
def solution_old2(n):
    answer = 0
    arr = [-1 for _ in range(1000001)]
    # arr[0] = 0
    # arr[1] = 1

    def sol(i):
        if i < 2:
            return i
        # 기저사례 2.
        if arr[n] != -1:
            return arr[n]
        arr[i] = sol(i - 2) + sol(i - 1)
        return arr[i]
        # sol(1) + sol(0)

    answer = sol(n)
    return answer

def solution_old3(n):
    sqrt_5 = 5 ** (1 / 2)
    ans = 1 / sqrt_5 * (((1 + sqrt_5) / 2) ** n - ((1 - sqrt_5) / 2) ** n)
    return int(ans)  % 1234567;

def fibonacci(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(fibonacci(3))


# 행렬 곱셈을 활용한 풀이
print(solution_old(5))
