def solution(record):
    answer = []
    id_map = {
        'Enter': '님이 들어왔습니다.',
        'Leave': '님이 나갔습니다.'
    }
    lst = []
    temp = [string.split(' ') for string in record]
    for t in temp:
        if t[0] == 'Enter':
            id_map[t[1]] = t[2]
        elif t[0] == 'Change':
            id_map[t[1]] = t[2]

        if t[0] != 'Change':
            lst.append((t[0], t[1]))

    for key, ids in lst:
        answer.append('{}{}'.format(id_map[ids], id_map[key]))
    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(record))
