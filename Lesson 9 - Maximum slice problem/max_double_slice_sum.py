""" MaxDoubleSliceSum
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N)
"""

def solution(A):
    N = len(A)
    # Initialise arrays for sum of slices that end and start at index position.
    slice1 = [0] * N
    slice2 = [0] * N

    # Calculate sum of slices that end at i.
    for i in range(1, N):
       tmp = slice1[i-1] + A[i]
       slice1[i] = max(tmp, 0)

    # Calculate sum of slices that begin at j.
    for j in range(N-2, 0, -1):
        tmp = slice2[j+1] + A[j]
        slice2[j] = max(tmp, 0)

    max_dbl_slice = 0
    # Calculate double slices that have k as the middle index.
    # Keep track of maximum value seen.
    for k in range(1, N-1):
        tmp = slice1[k-1] + slice2[k+1]
        max_dbl_slice = max(max_dbl_slice, tmp)

    return max_dbl_slice