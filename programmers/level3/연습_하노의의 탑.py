def solution(n):
    answer = []


    # n : 옮기려는 원반의 개수
    # from_pos : 옮길 원반이 현재 있는 출발점 기둥
    # to_pos : 원반을 옮길 도착점 기둥
    # aux_pos : 옮기는 과정에서 사용할 보조 기둥
    def hanoi(n, from_pos, to_pos, aux_pos):
        if n == 1:  # 원반이 1개라면 그냥 옮기자
            # print(from_pos, '->', to_pos)
            answer.append([from_pos, to_pos])
            return

        # 원반 n-1개를 aux_pos 로 이동
        hanoi(n-1, from_pos, aux_pos, to_pos)

        # 가장 큰 원바을 목적지로 이동
        # print(from_pos, '->', to_pos)
        answer.append([from_pos, to_pos])

        # aux_pos에 있는 원반 n-1개를 목적지로 이동
        hanoi(n-1, aux_pos, to_pos, from_pos)

    hanoi(n, 1, 3, 2)

    return answer