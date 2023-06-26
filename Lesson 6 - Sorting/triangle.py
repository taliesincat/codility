""" Triangle
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N*log(N))
"""

def solution(A):
    N = len(A)
    # If there are fewer than 3 values in A, there can't be a triplet
    if N < 3 :
        return 0    
    A.sort() # Sort A so A[i] <= A[i+1] <= A[i+2]
    # If A[i] + A[i+1] > A[i+2], A[i+1] + A[i+2] > A[i] and A[i+2] + A[i] > A[i+1] must also be true
    for i in range(0, N-2):
        if A[i] + A[i+1] > A[i+2] :
            return 1
    return 0

""" Additional test input
    [-10, -9, -8, 7, 6, 5] - returned value = 1
    [-10, -9, -8, -7, -6, -5] - returned value = 0
"""