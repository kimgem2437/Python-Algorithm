def solution(d, budget):
    result = 0
    d = sorted(d)
    for i in range(len(d)):
        budget -= d[i]
        if budget == 0:
            result += 1
            break
        elif budget < 0:
            break
        result += 1
    return result
         