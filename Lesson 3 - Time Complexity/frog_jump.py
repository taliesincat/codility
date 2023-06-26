""" FrogJmp
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(1)
"""
def solution(X, Y, D):
    count = (Y - X) / D
    if count % 1 == 0 :
        return int(count)
    else :
        return int(count) + 1

""" Additional test input
    [5, 200, 8]
    [55, 1000000000, 105]
"""
