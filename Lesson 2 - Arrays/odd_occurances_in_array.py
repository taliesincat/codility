""" Odd occurances in array
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N) or O(N*log(N))
"""

def solution(A):
    tmp = set()    
    for i in A :
        if i not in tmp :
            tmp.add(i)
        else :
            tmp.remove(i)
    return tmp.pop()

""" Additional test input
    [1, 3, 5, 7, 9, 7, 5, 3, 1]
"""