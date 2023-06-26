""" FrogRiverOne
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N)
"""

def solution(X, A): 
    N = len(A)
    # Initialise a set for positions (no duplicates) and a value for seconds.
    positions = set() 
    seconds = 0
    # Add to positions if it's a new position.
    # Update seconds if required.
    for i in range(0, N): 
        if A[i] not in positions and A[i] <= X: 
            positions.add(A[i]) 
            seconds = i 
    # If the length of the positions array is the same as X, all positions have been covered by leaves
    # Otherwise, not all positions have been covered, so return -1. 
    if len(positions) == X: 
        return seconds
    else :
        return -1

""" Additional test input
    (2, [2,2,2,2,2]) - returned value = -1
"""