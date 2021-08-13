from collections import deque

INF = int(1e9)
global n
global m


def bfs(maps, node, visited):
    # node = [start, end]
    q = deque([node])

    x = [-1, 0, 1, 0]
    y = [0, 1, 0, -1]
    while q:
        s, e = q.popleft()
        # print('queue 에서 pop : [{}, {}]'.format(s,e))

        for i in range(4):
            dx = s + x[i]
            dy = e + y[i]
            # print('dx, dy : [{}, {}]'.format(dx, dy))
            if 0 <= dx < n and 0 <= dy < m and maps[dx][dy] == 1:
                if visited[dx][dy] == -1:
                    visited[dx][dy] = visited[s][e] + 1
                    q.append([dx, dy])

    return visited[n - 1][m - 1]


def solution(maps):
    global n
    global m
    n = len(maps)
    m = len(maps[0])
    visited = [[-1] * m for _ in range(n)]
    visited[0][0] = 1

    answer = bfs(maps, [0, 0], visited)

    return answer


def solution_new(maps):
    d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    r = len(maps)
    c = len(maps[0])
    table = [[-1 for _ in range(c)] for _ in range(r)]
    q = deque()
    q.append([0, 0])
    table[0][0] = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + d[i][0]
            nx = x + d[i][1]

            if -1 < ny < r and -1 < nx < c:
                if maps[ny][nx] == 1:
                    if table[ny][nx] == -1:
                        table[ny][nx] = table[y][x] + 1
                        q.append([ny, nx])

    answer = table[-1][-1]
    return answer


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
print(solution(maps))
print(solution_new(maps))
