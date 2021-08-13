def solution(w, h):
    if w == h: return (w * h - w)
    
    # 최대공약수 gcd 알고리즘
    def gcd(a, b):
        if b == 0: return a
        return gcd(b, a % b)


    if w > h:
        w, h = h, w

    g = gcd(w, h)
    return w * h - (w + h - g)


w = 8
h = 12
print(solution(w, h))
