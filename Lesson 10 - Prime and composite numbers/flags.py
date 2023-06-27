""" Flags
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N)
"""

def solution(A):
    N = len(A)
    next_peak = [-1] * (N)
    peak_count = 0
    first_peak = -1

    # Generate index position of next peak from current index position.
    # Calculate in reverse from end of A.
    for i in range(N-2, 0, -1):
        if A[i-1] < A[i] > A[i+1]:
            next_peak[i] = i
            peak_count += 1
            first_peak = i
        else:
            next_peak[i] = next_peak[i+1]

    # If there are 0 or 1 peaks:
    if peak_count <= 1 :
        return peak_count

    # Initialise
    max_flags = 1
    distance = 1
    # Try for every valid distance between flags.
    # Distance for K flags requires K*(K-1) <= N.
    while distance * (distance-1) <= N:
        # Total number of available flags.
        flags = distance
        # Place one flag at the first peak.
        pos = first_peak
        placed_flags = 1
        flags -= placed_flags
        # while there are still available flags to place.
        while flags > 0 :
            if pos + distance >= N-1:
                # Gone beyond the end of the array of peaks.
                # Break out of while loop.
                break
            # Go to next available qualifying peak.
            pos = next_peak[pos+distance]
            if pos == -1 :
                # No more available peaks.
                # Break out of while loop.
                break
            # Place a flag on next available qualifying peak.
            placed_flags += 1
            # Subtract one from available flags.
            flags -= 1
        
        # Update max flags.
        max_flags = max(max_flags, placed_flags)
        # Increment distance.
        distance += 1

    return max_flags

""" Additional test input
    [7, 10, 4, 5, 7, 4, 6, 1, 4, 3, 3, 7] - returned value = 3
"""