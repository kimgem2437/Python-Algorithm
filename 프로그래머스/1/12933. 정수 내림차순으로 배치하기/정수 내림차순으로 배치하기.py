def solution(n):
    answer = sorted(str(n))
    return int(''.join(answer[::-1]))