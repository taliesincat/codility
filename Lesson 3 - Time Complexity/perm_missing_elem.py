""" PermMissingElem
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N) or O(N * log(N))
"""
def solution(A):
    # Sort the list of numbers in ascending order
    sort_A = sorted(A)
    # Initialize "missing" as 1.
    missing = 1
    # Iterate through the list.
    for i in sort_A:
        if i > missing:
            return missing
        missing += 1
    # If the missing number wasn't found, "missing" will be the value of the missing number.
    
    return missing

""" Additional test input
    []
    [10,9,8,6,5,4,3,2,1]
"""
