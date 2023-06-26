""" CountDiv
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(1)
"""

def solution(A, B, K):
    K_in_B = ((B // K) + 1)
    K_in_A = ((A // K) + 1)
    # Subtract the count of integers between 0 and A that are divisible by K from the the count of integers between 0 and B that are divisible by K
    num_K = K_in_B - K_in_A

    # A is inclusive, so if it is divisible by K then include in result by adding 1 to the result
    if A % K == 0 :
        num_K += 1

    return num_K

""" Additional test input
    [0, 2000000000, 2000000000] - returned value = 2
    [10, 2000000000, 2000000000] - returned value = 1
    [0, 0, 11] - returned value = 1
    [10, 10, 20] - returned value = 1
    [5, 10, 20]  - returned value = 0
    [1, 1, 11] - returned value = 0
    [2, 10, 2] - returned value = 5
    [2, 11, 2] - returned value = 5
    [1, 10, 2] - returned value = 5
    [11, 345, 17] - returned value = 20
"""
