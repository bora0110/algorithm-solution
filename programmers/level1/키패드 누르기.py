def solution(numbers, hand):
    answer = ''

    bef_left = '*'
    bef_right = '#'

    map = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        '*': [3, 0], 0: [3, 1], '#': [3, 2]
    }

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            bef_left = num
        elif num in [3, 6, 9]:
            answer += 'R'
            bef_right = num
        else:
            now = map[num]
            bef_left_posi = map[bef_left]
            bef_right_posi = map[bef_right]

            left_num = abs(bef_left_posi[0] - now[0]) + abs(bef_left_posi[1] - now[1])
            right_num = abs(bef_right_posi[0] - now[0]) + abs(bef_right_posi[1] - now[1])

            print("now:" + str(num) + ", left_num:" + str(left_num) + ", right_num:" + str(right_num))
            if left_num < right_num:
                answer += 'L'
                bef_left = num
            elif left_num > right_num:
                answer += 'R'
                bef_right = num
            else:
                if hand == 'right':
                    answer += 'R'
                    bef_right = num
                else:
                    answer += 'L'
                    bef_left = num

    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))
