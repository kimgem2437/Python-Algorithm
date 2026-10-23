def solution(sizes):
    maxW = 0
    maxH = 0
    for i in range(len(sizes)):
        maxSize = max(sizes[i][0], sizes[i][1])
        minSize = min(sizes[i][0], sizes[i][1])
        sizes[i][0] = maxSize
        sizes[i][1] = minSize
        
        if maxW < sizes[i][0]:
            maxW = sizes[i][0]
        if maxH < sizes[i][1]:
            maxH = sizes[i][1]
    return maxW * maxH
        