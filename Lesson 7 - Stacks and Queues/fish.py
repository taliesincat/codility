""" Fish
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N)
"""

def solution(A, B):
    N = len(A)    
    surviving = 0
    downstream = list()

    for i in range(N):
        # If a fish is travelling downstream, add it to the downstream list
        if B[i] == 1 :
            downstream.append(A[i])
        # If a fish is travelling upstream
        else:
            # While there are fish travelling downstream that are upstream of fish i, work out who eats who
            while len(downstream) > 0 :
                if downstream[-1] < A[i] :
                    downstream.pop()
                else:
                    # Break out of while loop if there are no more fish travelling downstream that are upstream of fish i
                    break
            # If there are no fish travelling downstream that are upstream of fish i, add 1 to number of surviving fish
            else: 
                surviving += 1
    
    surviving += len(downstream) # Add any fish remaining in the downstream list to the list of surviving fish
    return surviving

""" Additional test input
    ([1,2,3,4,5,6,7,8,9,10], [1,1,1,1,1,1,1,1,1,1]) - returned value = 10
    ([10,9,8,7,6,5,4,3,2,1], [0,1,0,1,0,1,0,1,0,1]) - returned value = 6
    ([100], [0]) - returned value = 1
    ([10,9,8,7,6,5,4,3,2,1], [0,0,0,0,0,1,1,1,1,1]) - returned value = 10
    ([10, 9, 10, 9, 10, 9], [0, 1, 0, 1, 0, 1]) - returned value = 4
"""


