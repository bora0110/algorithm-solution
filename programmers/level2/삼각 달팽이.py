# 삼각 달팽이
def solution(n):
    # n을 변으로 가지는 이등변직각삼각형 만들기
    triangle = [[0 for i in range(0, j)] for j in range(1, n + 1)]
    print(triangle)
    # 숫자 채우기
    # 행
    x = -1
    # 열
    y = 0
    # 넣을 수
    k = 1
    # 행 접근
    for a in range(n):
        # 열 접근
        for b in range(a, n):
            if a % 3 == 0:
                x += 1
            elif a % 3 == 1:
                y += 1
            elif a % 3 == 2:
                x -= 1
                y -= 1
            triangle[x][y] = k
            k += 1

    # 1차원 리스트로 변환
    # print(triangle)
    answer = sum(triangle, [])  # 2차원 배열을 sun(배열, []) 하면 1차원 배열로 변경됨
    return answer

print(solution(4))