def solution(n, times):
    answer = 0
    # 최소시간, 최대시간 구하기
    # 최대시간 = 가장 오래걸리는 심사관이 계속 검사
    # 최소+최대 값의 중간값인 mid 가 n명을 심사할 수 잇는지 파악하며 이분 탐색 진행
    # n명을 심사할 수 있다면 답을 갱신하고, 최대범위를 줄이기
    # n명을 심하할 수 없다면, 최소범위를 늘리기

    left = 1
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2

        count = 0
        for time in times:
            count += mid // time

            # 심사 인원수를 넘으면 다음 단계
            if count >= n:
                break
        # n명을 심사할 수 있는 경우
        # 한 심사관에게 주어진 시간을 줄여본다
        if count >= n:
            answer = mid
            right = mid - 1
        # 없는 경우
        elif count < n:
            left = mid + 1

    return answer