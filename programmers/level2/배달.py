import heapq

INF = int(1e9)


def dijkstra(start):
    q = []

    heapq.heappush(q, (start, 0))
    visited[start] = 0
    # [[], [(2, 1), (4, 2)], [(3, 3)], [], [], [(2, 2), (3, 1), (4, 2)]]
    while q:
        node, score = heapq.heappop(q)

        if visited[node] < score:
            continue

        for i in graph[node]:
            n, s = i
            cost = score + s  # 이전 가중치 + 현재 노드까지의 가중치

            if cost <= max_k and cost < visited[n]:
                visited[n] = cost
                heapq.heappush(q, (n, cost))

def dijkstra2(start):
    q = []

    q.append((start, 0))
    visited[start] = 0

    # [[], [(2, 1), (4, 2)], [(3, 3)], [], [], [(2, 2), (3, 1), (4, 2)]]
    while q:
        node, score = q.pop()

        if visited[node] < score:
            continue

        for i in graph[node]:
            n, s = i
            cost = score + s  # 이전 가중치 + 현재 노드까지의 가중치

            if cost <= max_k and cost < visited[n]:
                visited[n] = cost
                q.append((n, cost))

def solution(N, road, K):
    answer = 0

    # N 마을 수
    # road 간선 수
    # K 한정된 시간

    global graph
    global visited
    global max_k

    graph = [[] for _ in range(N + 1)]  # 마을 수 만큼
    visited = [INF] * (N + 1)
    max_k = K
    for r in road:
        graph[r[0]].append((r[1], r[2]))
        graph[r[1]].append((r[0], r[2]))

    dijkstra(1)

    for v in visited:
        if v < INF:
            answer += 1
    return answer


aa = 5
bb = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
cc = 3

print(solution(aa, bb, cc))
'''
마을의 개수 N, 각 마을을 연결하는 도로의 정보 road
음식 배달이 가능한 시간 K가 매개변수로 주어질 때, 
음식 주문을 받을 수 있는 마을의 개수를 return 하도록 solution 함수를 완성해주세요.

마을의 개수 N은 1 이상 50 이하의 자연수입니다.
road의 길이(도로 정보의 개수)는 1 이상 2,000 이하입니다.
'''
