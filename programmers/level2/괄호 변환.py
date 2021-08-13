def solution(p):
    cnt = 0
    inner_cnt = 0

    if not p:
        return ''

    u = ''
    v = ''

    for s in p:
        if s == '(':
            cnt += 1
            u += s
        else:
            cnt -= 1
            u += s

        if cnt == 0:  # 균형잡힌 괄호
            v = p[len(u):]
            u_is_right = True

            for inner_p in u:
                if inner_p == '(':
                    inner_cnt += 1
                else:
                    inner_cnt -= 1
                if inner_cnt < 0:
                    u_is_right = False  # 균형잡혔지만 올바르진 않은 상태

            if u_is_right:  # 균형잡혔고, 올바른 상태면
                return u + solution(v)
            else:
                new_u = ''
                for i in u[1:-1]:  # 양쪽 맨끝을 제외하고 반복문
                    if i == '(':
                        new_u += ')'
                    else:
                        new_u += '('
                answer = '(' + solution(v) + ')' + new_u
                return answer


p = "()))((()"
print(solution(p))
