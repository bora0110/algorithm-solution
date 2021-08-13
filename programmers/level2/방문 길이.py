def solution(dirs):
    answer = 0

    dict = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visi_dic = {}

    dx, dy = 0, 0
    bdx, bdy = 0, 0
    for d in dirs:
        bdx, bdy = dx, dy
        temp_x, temp_y = dx, dy
        flag = False

        if d == "U":
            temp_x, temp_y = dx + dict[0][0], dy + dict[0][1]
        elif d == "D":
            temp_x, temp_y = dx + dict[1][0], dy + dict[1][1]
        elif d == "R":
            temp_x, temp_y = dx + dict[2][0], dy + dict[2][1]
        elif d == "L":
            temp_x, temp_y = dx + dict[3][0], dy + dict[3][1]

        if -5 <= temp_x <= 5 and -5 <= temp_y <= 5:
            flag = True
            dx, dy = temp_x, temp_y

        key = str(bdx) + str(bdy) + str(dx) + str(dy)
        key2 = str(dx) + str(dy) + str(bdx) + str(bdy)
        if flag and key not in visi_dic and key2 not in visi_dic:
            visi_dic[key] = True
            answer += 1

    return answer


def solution_new(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny

    # print(s)
    return len(s)//2


aa = "UDU"
print(solution(aa))
print(solution_new(aa))
