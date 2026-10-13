def solution(price, money, count):
    prices = 0
    for i in range(1, count + 1):
        prices += i * price
    if prices - money >= 0:
        return prices - money
    else:
        return 0
    