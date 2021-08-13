import re


def solution(files):
    answer = []
    # split(패턴, 문자열, 최대 split 수, 플래드)
    # temp = [re.split('\d{1:5}+', s) for s in files]
    # temp = sorted(files, key=lambda file: int(re.findall('\d+', file)[0]))
    temp = [re.split(r"([0-9]+)", s) for s in files]
    print(temp)

    sort = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))
    # print(sort)

    answer = ["".join(s) for s in sort]
    return answer


aa = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(aa))
