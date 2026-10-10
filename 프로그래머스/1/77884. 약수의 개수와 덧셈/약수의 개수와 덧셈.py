def solution(left, right):
    cnt = 0
    result = 0
    while left <= right:
        for i in range(1, left + 1):
            if left % i == 0:
                cnt += 1
        if cnt % 2 == 0:
            result += left
        else:
            result -= left
        left += 1
        cnt = 0
    return result