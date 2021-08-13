def solution(numbers):
    answer = ''
    numbers_str = [str(num) for num in numbers]  # 1. 사전 값으로 정렬하기
    print(numbers_str)
    numbers_str.sort(key=lambda num: num * 3, reverse=True)  # 2. number는 1000이하의 숫자이므로 x3(반복)한 값으로 비교
    print(numbers_str)
    answer = "".join(numbers_str)

    return str(int(answer))

n = [6, 10, 2]
print(solution(n))


'''
numbers_str.sort(key=lambda num: num * 3, reverse=True) 
[9,5,34,30,3]  정렬되는 것을
[999, 555, 343434, 303030, 333] 로 바꿔서
[999, 555, 343434, 333, 303030] 게 정렬하기 위함
'''