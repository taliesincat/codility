""" CountFactors
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(sqrt(N))
"""

def solution(N):
    # Initialise
    count = 0
    f = 1
    while f**2 < N :
        # If f is a factor of N, then add two to count (one for f, and one for whatever N/f is).
        if N % f == 0 :
            count += 2
        # Increment f
        f += 1

    # If f x f = N, add another to count
    if f**2 == N :
        count += 1

    return count

""" Additional test input
    0 - returned value = 0
    2147483647 - returned value = 2
    69 - returned value = 4
"""