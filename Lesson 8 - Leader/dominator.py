""" Dominator
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N*log(N)) or O(N)
"""
def solution(A):
    N = len(A)
    # If there's nothing in A, there is no dominator
    if N == 0 :
        return -1

    # Initialise variables for candidate dominator, count of how many occurances of the current candidate there have been, and the index of the current candidate
    candidate = -1
    candidate_count = 0
    candidate_index = -1
    
    # Find a candidate
    # Add or subtract from candidate_count depending on what the next number is
    for i in range(N) :
        # If there's currently no candidate, pick the current number as the candidate
        if candidate_count == 0 :
            candidate = A[i]
            candidate_index = i
            candidate_count += 1        
        else :
            # If current number is the candidate, add 1 to occurances of candidate
            if A[i] == candidate :
                candidate_count += 1
            # If current number is not the candidate, subtract 1 to occurances of candidate
            else :
                candidate_count -= 1

    # Loop through array again to count how many instances of the candidate there are in total
    count = 0
    for i in range(N):
        if A[i] == candidate :
            count += 1
    
    # Work out if the candidate occures in more than have the elements of A
    if count <= N // 2:
        return -1
    else:
        return candidate_index

""" Additional test input
    [] - returned value = -1
    [1] - returned value = 0
    [1,1,1,2,3,4,5,6,1,1,1,1,7,8,9] - returned value = -1
    [1,1,2,1,1,2,3,2,1,1,3,5,3,1] - returned value = -1
    [9,9,9,9,9,9,9,9] - returned value = 0
"""