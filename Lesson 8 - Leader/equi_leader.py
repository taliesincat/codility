""" EquiLeader
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N)
"""

def solution(A):
    N = len(A)
    # If there's nothing in A, there is no equileader
    if N == 0 :
        return -1

    # Initialise variables for candidate equileader and count of how many occurances of the current candidate there have been
    candidate = -1
    candidate_count = 0
        
    # Find a candidate
    # Add or subtract from candidate_count depending on what the next number is
    for i in range(N) :
        # If there's currently no candidate, pick the current number as the candidate
        if candidate_count == 0 :
            candidate = A[i]
            candidate_count += 1
        else :
            # If current number is the candidate, add 1 to occurances of candidate
            if A[i] == candidate :
                candidate_count += 1
            # If current number is not the candidate, subtract 1 to occurances of candidate
            else :
                candidate_count -= 1

    # Loop through again to count how many instances of the candidate there are in total
    count_leaders = 0
    for j in range(N):
        if A[j] == candidate :
            count_leaders += 1

    # Work out if the candidate occures in more than have the elements of A
    if count_leaders <= N // 2:
        # Didn't find a leader, there are no equileaders
        return 0
    else:
        # Found a leader!
        leader = candidate

    equi_leaders = 0
    leaders_in_section = 0

    for k in range(N) :
        # If this is a leader, add to count
        if A[k] == leader :
            leaders_in_section += 1
        # If the section this value in has a leader, and if the remaining part of the list also has a leader, then there is an equileader
        if leaders_in_section > (k+1) // 2 and ((count_leaders - leaders_in_section) > (N-k-1) // 2):
            equi_leaders += 1

    return equi_leaders
    
""" Additional test input
    [1,1,1,1,1,1,1,1,9,9,9] - returned value = 4
    [1] - returned value = 0
    [] - returned value = -1
    [1,2,1,3,1,4,1,5,1,6,1,7,1] - returned value = 0
    [1,2] - returned value = 0
"""