import itertools
import operator


def solution(orders, course):
    answer = []
    dic = {}

    for order in orders:
        # print('주문 : ', order)

        for cour in course:
            if cour not in dic:
                dic[cour] = {}

            # print('코스 : ', cour)
            for menu in itertools.combinations(order, cour):
                menu_str = "".join(sorted(list(menu)))

                dic[cour][menu_str] = dic[cour].get(menu_str, 0) + 1

    for d in dic.values():
        # 값 기준(key=operator.itemgetter(1)) 내림차순으로 정렬
        sdic = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
        print(sdic)
        if sdic:
            max_value = sdic[0][1]
            # 최대 주문 수가 2 미만인 겨우 패스
            if max_value < 2:
                continue
            for d2 in sdic:
                if d2[1] == max_value:
                    answer.append(d2[0])

    answer.sort()
    return answer


o = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
c = [2, 3, 5]

print(solution(o, c))

'''

아이디어
각 주문내역에 대한 조합(>2) 을 만들고
코스 수 만큼 반복문을 돌려서

코스가 2,3,4 가 있으면
각 주문내역에 대한 2조합, 3조합, 4조합을 만들어
그리고 딕셔너리에 그 조합이 호출된걸 +1 시켜줘 

반복문 돌면서 호출(주문) 건수가 0이상한 것들만 결과로 넘겨

 {'12': 1, '13': 1, '14': 1, '23': 1, '24': 1, '34': 1}

'''
