""" MaxProductOfThree
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N * log(N))
"""

def solution(A):
    A.sort(reverse=True) # Sort A, largest first
    top_3 = (A[0] * A[1] * A[2]) # Compare the product of the three largest integers.
    # Also compare the product of the largest and two smallest integers, in case the two smallest integers are negative numbers with a large (positive) product
    top_1_bottom_2 = (A[0] * A[-2] * A[-1])
    
    return max(top_3, top_1_bottom_2) # return the largest of the two calculated values.

""" Additional test input
    [-5, -4, 3, 2, 4, -9] - returned value = 180
    [-5, -5, 4, 3, 2] - returned value = 100
"""