""" Cyclic rotation
    
    Task score: 100%
    Correctness: 100%
    Performance: Not assessed
"""
def solution(A, K):
    a = len(A) - 1
    try: 
        for i in range(0,K) :
            tmp = list()
            tmp.append(A[a])
            for j in range(0, a) :
                tmp.append(A[j])
            A = tmp
        return A
    except:
        return A

""" Additional test input
    ([], 4)
"""
