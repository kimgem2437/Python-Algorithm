def solution(n, m):
    answer = []
    a, b = n, m
    while b:
        a, b = b, a % b
    gcd = a
    lcd = n * m // gcd
    return [gcd, lcd]