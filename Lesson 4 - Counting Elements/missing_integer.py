""" MissingInteger
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N) or O(N * log(N))
"""

def solution(A):
    A = set(A) # Remove duplicate values.    
    count = 1 # Initialise "count" as the smallest possible +ve integer.    
    while count in A: # Search for "count" in A, increment "count" if it's found, and search again
        count += 1
    # As soon as "count" isn't found in A, return "count"
    return count

""" Additional test input
    [-3, -2, -1, 1, 2, 3, 5, 6, 7] - returned value = 4
    [2, 3, 4, 5, 6] - returned value = 1
"""
