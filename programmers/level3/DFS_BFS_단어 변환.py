from collections import deque


def solution(begin, target, words):
    visited = {}
    visited[begin] = 0
    q = deque()
    q.append(begin)
    word = ""
    while q:
        word = q.popleft()
        if word == target:
            break

        for diff_w in words:
            diff_cnt = 0
            if diff_w in visited:
                continue
            for idx in range(len(diff_w)):
                if diff_cnt > 1:
                    break
                if word[idx] != diff_w[idx]:
                    diff_cnt += 1
            if diff_cnt == 1:
                q.append(diff_w)
                visited[diff_w] = visited[word] + 1
    # print(visited)
    if target in visited:
        return visited[target]
    else:
        return 0