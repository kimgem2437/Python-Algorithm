def solution(arr):
    
    result = 0
    cnt = 0
    for i in range(len(arr)):
        result += arr[i]
        
    result /= len(arr)
    return result