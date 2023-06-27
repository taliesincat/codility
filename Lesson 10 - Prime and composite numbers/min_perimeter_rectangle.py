""" CountFactors
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(sqrt(N))
"""

def solution(N):
    # These are potential lengths of the sides A and B to make rectangle of area N.
    A = list()
    B = list()

    f = 1
    while f**2 <= N :
        # If f is a factor, append f to A and N/f to B.
        if N % f == 0 :
            A.append(f)
            B.append(N / f)
        f += 1

    # Initialise minimal perimeter value.
    perimeter = None
    # Calculate perimeters for all pairs of factors.
    # Update minimal perimeter value if appropriate.
    M = len(A)
    for i in range(0, M) :
        if perimeter == None :
            perimeter = 2*(A[i] + B[i])
        if 2*(A[i] + B[i]) < perimeter :
            perimeter = 2*(A[i] + B[i])
    
    # Return as an integer.
    return int(perimeter)

""" Additional test input
    100 - returned value = 40
    625 - returned value = 100
    500 - returned value = 90
    1000000000 - returned value = 126500
"""