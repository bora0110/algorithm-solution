import itertools


def solution(places):
    answer = []

    def check(p1, p2, place):
        distance = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

        # print('({},{}) = ({},{}) => {}'.format(p1[0], p1[1], p2[0], p2[1], distance))
        if distance == 1:
            return False
        elif distance > 2:
            return True
        else:  # 맨하탄거리가 2이하 일 때 정합성 확인 필요! (파이션이 있어야 앉을 수 있다)
            is_partition = False

            if p1[0] == p2[0]:  # 같은 x축에 있으면
                if place[p1[0]][p1[1]+1] == 'X':
                    is_partition = True
            elif p1[1] == p2[1]:  # 같은 Y축에 있으면
                if place[p1[0]+1][p1[1]] == 'X':
                    is_partition = True
            else:
                if place[p1[0]][p2[1]] == 'X' and place[p2[0]][p1[1]] == 'X':
                    is_partition = True

            return is_partition

    for place in places:
        print(place)

        p_arr = []
        for x_idx, row_data in enumerate(place):
            for y_idx, data in enumerate(row_data):
                if data == 'P':
                    p_arr.append((x_idx, y_idx))
        # print(p_arr)

        # nn = list(itertools.combinations(p_arr, 2))
        # print(nn)

        flag = True
        p_cnt = len(p_arr)
        for x in range(p_cnt):
            for y in range(x+1, p_cnt):
                # print('({}) = ({})'.format(p_arr[x], p_arr[y]))
                if not check(p_arr[x],  p_arr[y], place):
                    flag = False
                    break

        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))