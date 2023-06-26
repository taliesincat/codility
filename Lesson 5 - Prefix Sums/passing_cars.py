""" PassingCars
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N)
"""

def solution(A):    
    Q = A.count(1) # Count the number of cars going west (how many times the value in A is 1.)     
    pairs = 0 # Initialise number of pairs as 0

    for value in A:
        # If value = 0, this is a car travelling east, and can form a pair with all cars travelling west (Q).
        if value == 0 :
            pairs += Q
        # When value is 1, this is a car travelling west.
        # Remove this car from Q for further loops.
        else: 
            Q -= 1
    # return -1 if the number of pairs of passing cars exceeds 1,000,000,000
    if pairs > 1000000000 :
        pairs = -1
    return pairs

""" Additional test input
    [0, 0, 0, 0, 0] - returned value = 0
    [1, 1, 1, 1, 1] - returned value = 0
    [0, 1, 0, 0, 0] - returned value = 1
"""