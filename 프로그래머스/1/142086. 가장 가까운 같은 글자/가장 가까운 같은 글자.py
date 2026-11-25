def solution(s):
    last = {}
    answer = []
    for i, c in enumerate(s):
        answer.append(i - last[c] if c in last else -1)
        last[c] = i
    return answer