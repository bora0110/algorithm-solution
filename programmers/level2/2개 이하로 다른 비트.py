def solution_old(numbers):  # 일일히 비교하는 것은 시간 초과
    answer = [0]*len(numbers)
    cnt = [0] * len(numbers)

    for idx, num in enumerate(numbers):
        str = bin(num)
        str = list(str[2:])
        str.reverse()
        # print('{} = {}'.format(num, str))
        num2 = num
        while True:
            num2 += 1
            cnt[idx] = 0
            str1 = list(bin(num2)[2:])
            str1.reverse()
            # print('{} = {}'.format(num2, str1))

            for i, j in zip(str, str1):
                if i != j:
                    cnt[idx] += 1

            cnt[idx] += abs(len(str) - len(str1))

            if 0 <= cnt[idx] <= 2:
                answer[idx] = num2
                break
        # print(cnt)

    return answer

'''
짝수인 경우
맨 끝 자리가 무조건 0이기 떄문에 1로 바꿔서 10진수로 변환

홀수인 경우
처음 나오는 0을 1로 바꾸고 10진수로 변환

10진수->2진수 bin(숫자)
2진수->10진수 int(숫자, 2)
'''
def solution_new(numbers):  # 일일히 비교하는 것은 시간 초과
    answer = [0]*len(numbers)

    for idx, num in enumerate(numbers):
        if num%2 == 0:  # 짝수
            lst = list(bin(num)[2:])
            lst[-1] = '1'
        else:  # 홀수
            lst = ['0'] + list(bin(num)[2:])
            # print(lst)
            # ['0', '1', '1', '1', '1', '1', '0', '1', '0', '0', '1']
            idx2 = ''.join(lst).rfind('0')
            idx3 = ''.join(lst).find('1', idx2)
            lst[idx2], lst[idx3] = lst[idx3], lst[idx2]

        answer[idx] = int(''.join(lst), 2)

    return answer

numbers = [1001,337,0,1,333,673,343,221,898,997,121,1015,665,779,891,421,222,256,512,128,100]
# [1002, 338, 1, 2, 334, 674, 347, 222, 899, 998, 122, 1019, 666, 781, 893, 422, 223, 257, 513, 129, 101]
print(solution_old(numbers))
print(solution_new(numbers))