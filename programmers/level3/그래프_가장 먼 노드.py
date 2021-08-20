from collections import deque


def solution(n, edge):
    answer = 0
    visited = [-1] * (n + 1)
    graph = {}

    for e in edge:
        graph[e[0]] = graph.get(e[0], []) + [e[1]]
        graph[e[1]] = graph.get(e[1], []) + [e[0]]

    q = deque()
    q.append([1, 0])  # [노드번호, 길이]

    while q:
        node = q.popleft()
        v = node[0]
        leng = node[1]

        if visited[v] == -1:  # 방문 안했으면
            visited[v] = leng
            leng += 1
            for e in graph[v]:
                q.append([e, leng])

    max_leng = max(visited)
    for v in visited:
        if v == max_leng:
            answer += 1

    return answer