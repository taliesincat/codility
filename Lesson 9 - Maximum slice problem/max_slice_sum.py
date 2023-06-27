""" MaxSliceSum
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N)
"""

def solution(A):
    N = len(A)
    # For arrays of length 0 and 1
    if N == 0 :
        return 0
    if N == 1 :
        return A[0]

    # Initialise local and overall maxima
    local_max = A[0]
    max_sum = A[0]

    # Compare current value against local maximum, update local max and overall max if applicable.
    for i in range(1,N) :
        local_max = max(A[i], (local_max + A[i]))
        max_sum = max(max_sum, local_max)
    
    return max_sum

""" Additional test input
    [-1, 10, -2, 13, -3, 15] - returned value = 33
    [] - returned value = 0
    [-1] - returned value = -1
    [1,-2,3,-4,5,-6,7,-8,9,-1,3] - returned value = 11
    [10, -9, -1, -3, -5, 18] - returned value = 18
"""