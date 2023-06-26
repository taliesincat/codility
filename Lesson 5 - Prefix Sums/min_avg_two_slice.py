""" MinAvgTwoSlice
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N)
"""

def solution(A):
    # Assuming that the slice that has the minimal average value is length 2 or 3.
    # All longer slices that also have the minimal average are built up of these 2 or 3 length small slices.
        
    N = len(A)
    # Initialise for A[0:1] (the only guarenteed possible slice)
    min_pos = 0
    min_avg = ((A[0] + A[1]) / 2)
    avg = 0

    for i in range(0, N-2) :
        # check the first two-element slice
        avg = (A[i] + A[i + 1]) / 2
        if avg < min_avg :
            min_avg = avg
            min_pos = i
        
        # check the 3-element slice
        avg = (A[i] + A[i+1] + A[i+2]) / 3
        if avg < min_avg :
            min_avg = avg
            min_pos = i

    # check the last two-element array that the for loop doesn't cover
    avg = (A[N-2] + A[N-1]) / 2
    if avg < min_avg :
        min_avg = avg
        min_pos = N-2

    return min_pos

""" Additional test input
    [-1, -2, 4, 2, 2, 5, 1, 5, 8] - returned value = 0
    [-2, -4, -6, -8, 10] - returned value = 2
    [-4, 10, -2, 5, -1, 5, -8] - returned value = 5
"""

#
#
#
