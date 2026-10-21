def solution(s):
    answer = ""
    cnt = 0
    for ch in s:
        if ch == " ":
            answer += ch
            cnt = 0      
        else:
            answer += ch.upper() if cnt % 2 == 0 else ch.lower()
            cnt += 1
    return answer