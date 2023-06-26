""" Distinct
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N*log(N)) or O(N)
"""

def solution(A):
    # Sets cant have duplicates, so if A gets put into a set, the length of the set is the number of distinct values in A.
    set_a = set(A) 
    return len(set_a)
