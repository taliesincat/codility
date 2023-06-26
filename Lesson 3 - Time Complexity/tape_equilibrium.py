""" Tape Equilibrium
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N)
"""

def solution(A):
    differences = list()
    left = 0
    tot = sum(A)
    # For each value in A, subtract it from "tot" and add it to "left".
    # Append this value to "differences".
    for i in range(0,len(A)-1):
        left += A[i]
        tot -= A[i]
        differences.append(abs(tot - left))
    # Return the minimum of "differences".
    return min(differences)

""" Additional test input
    [8, 4, 9, 2, 6]
"""
