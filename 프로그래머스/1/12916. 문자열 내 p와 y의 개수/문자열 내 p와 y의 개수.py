def solution(s):
    s = s.upper()
    pcnt = 0
    ycnt = 0
    for i in range(len(s)):
        if s[i] == 'P':
            pcnt += 1
        elif s[i] == 'Y':
            ycnt += 1
    return pcnt == ycnt
