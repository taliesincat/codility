""" PermCheck
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N) or O(N * log(N))
"""

def solution(A):
    # Transform A into a set to ensure each element is only there once.
    # If the maximum value of the set is equal to the length of the array, and the length of the set and the length of the list are the same, A is a permutation.
    set_a = set(A)
    if max(set_a) == len(A) and len(set_a) == len(A) :
        return 1
    else :
        return 0
    
""" Additional test input
    [9, 5, 7, 3, 2, 7, 3, 1, 10, 8] - returned value = 0
    [1, 5, 7, 8, 2, 3, 10, 4, 9] - returned value = 0
    [1, 5, 7, 8, 2, 3, 6, 10, 4, 9] - returned value = 1
    [1, 1, 1, 5, 2, 3, 6, 10, 4, 9] - returned value = 0
"""
