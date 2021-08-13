def solution(clothes):
    map = {}
    for u in clothes:
        if u[1] in map:
            # key 존재
            map[u[1]].append(u[0])
        else:
            map[u[1]] = [u[0]]

    # print(map)

    result = 1
    for u in map:
        result = result * (len(map[u]) + 1)

    return result - 1


clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
