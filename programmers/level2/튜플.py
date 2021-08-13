import re
from collections import Counter


def solution(s):
    s = Counter(re.findall('\d+', s))  # 숫자만 찾아서 리스트형으로 생성 후 counter
    print(s)
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))


# [2, 1, 3, 4]

a = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(a))
print(solution_new(a))
