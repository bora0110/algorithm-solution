def calc(op, idx, expression):
    result = 0
    if expression.isdigit():  # 더이상 exp에 연산자가 없으면
        return str(expression)  # 그대로 리턴
    else:
        if op[idx] == '*':

            split_data = expression.split("*")  # 연산자로 쪼갬
            temp = []
            for s in split_data:  # 쪼개진 각 부분에 대해 재귀
                temp.append(calc(op, idx + 1, s))
            return str(eval("*".join(temp)))  # 재귀 실행 결과를 담은 배열에 대해 eval()함수로 계산

        elif op[idx] == '+':
            split_data = expression.split("+")  # 연산자로 쪼갬
            temp = []
            for s in split_data:  # 쪼개진 각 부분에 대해 재귀
                temp.append(calc(op, idx + 1, s))
            return str(eval("+".join(temp)))  # 재귀 실행 결과를 담은 배열에 대해 eval()함수로 계산

        elif op[idx] == '-':
            split_data = expression.split("-")  # 연산자로 쪼갬
            temp = []
            for s in split_data:  # 쪼개진 각 부분에 대해 재귀
                temp.append(calc(op, idx + 1, s))
            return str(eval("-".join(temp)))  # 재귀 실행 결과를 담은 배열에 대해 eval()함수로 계산

    return result


def solution(expression):
    answer = 0

    # 6가지 operation 정의
    operations = [('*', '+', '-'), ('*', '-', '+'), ('+', '*', '-'), ('+', '-', '*'), ('-', '+', '*'), ('-', '*', '+')]

    for op in operations:  # 정의된 op에 따라 calc 재귀 진행

        result = abs(int(calc(op, 0, expression)))  # 얻어낸 결과값에 대해 절대값 취함.

        if result > answer:  # 기존의 결과값과 비교
            answer = result

    return answer


e = "100-200*300-500+20"
print(solution(e))
