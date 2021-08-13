import heapq as hq


def solution(scoville, K):
    hq.heapify(scoville)  # 리스트를 힙으로
    answer = 0

    while True:
        first = hq.heappop(scoville) # 가장 작은 원소를 삭제 후 그 값을 리턴
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second * 2)
        answer += 1

    return answer


arr = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(arr, k))
