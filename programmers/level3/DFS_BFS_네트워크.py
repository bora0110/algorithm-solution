from collections import deque


def solution_old(n, computers):
    answer = 0
    visi = [-1] * n
    graph = [[] for _ in range(n)]

    # print(visi)
    # print(graph)
    # print(computers)

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)
    # print(graph)

    q = deque()
    q.append(0)
    answer = 1
    visi_cnt = 0
    while q or visi_cnt != n:
        if not q:
            answer += 1
            no_visi_com_idx = visi.index(-1)
            q.append(no_visi_com_idx)
        com = q.popleft()

        for link_com in graph[com]:
            if visi[link_com] == -1:
                visi_cnt += 1
                q.append(link_com)
                visi[link_com] = 1
    return answer


def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]

    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] == 1 and visited[i] == 0:
                    stack.append(i)

    i = 0
    while 0 in visited:
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
        i += 1

    def solution_old(n, computers):
        answer = 0
        visi = [-1] * n
        graph = [[] for _ in range(n)]

        # print(visi)
        # print(graph)
        # print(computers)

        for i in range(n):
            for j in range(n):
                if computers[i][j] == 1:
                    graph[i].append(j)
        # print(graph)

        q = deque()
        q.append(0)
        answer = 1
        visi_cnt = 0
        while q or visi_cnt != n:
            if not q:
                answer += 1
                no_visi_com_idx = visi.index(-1)
                q.append(no_visi_com_idx)
            com = q.popleft()

            for link_com in graph[com]:
                if visi[link_com] == -1:
                    visi_cnt += 1
                    q.append(link_com)
                    visi[link_com] = 1
        return answer
    return answer