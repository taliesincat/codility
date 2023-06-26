""" GenomicRangeQuery
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N + M)
"""

def solution(S, P, Q):
    M = len(P)
    impact_factors = list() # List of impact factors   

    for x in range(0, M):
        p = P[x]
        q = Q[x]
        S_interest = S[p:q+1] # Part of string S that is of interest

        # Look for nucleotides and append appropriate impact factor to list depending on what nucleotides are present in S_interest
        if 'A' in S_interest :
            impact_factors.append(1)
        elif 'C' in S_interest :
            impact_factors.append(2)
        elif 'G' in S_interest :
            impact_factors.append(3)
        else :
            impact_factors.append(4)

    return impact_factors

""" Additional test input
    ('CAGCCTACAGCCTACAGCCTACAGCCTA', [1,3,5,7,1,5,7], [2,3,10,20,2,8,12]) - returned value [1, 2, 1, 1, 1, 1, 1]
    ('GGGGAGGGGG', [1,3,5,1,4], [6,5,6,8,9]) - returned value [1, 1, 3, 1, 1]
"""