""" CountNonDivisible
    
    Task score: 88%
    Correctness: 100%
    Performance: 75%
    Detected time complexity: O(N * log(N)) or O(N ** 2)
"""

def solution(A):
    N = len(A)
    max_A = max(A)
    
    # Count occurances of elements in A in dictionary: key is element in A, value is number of occurances
    occurances = dict()
    for element in A:
        occurances[element] = occurances.get(element, 0) + 1

    # Dictionary for the divisors for each element in occurances: key is element in A, value is list of divisors
    divisors = dict()    
    for element in occurances:
        divisors[element] = [1]

    i = 2
    # Iterate through integers below max_A
    while i <= max_A :
        j = i
        # Iterate through from i to max_A in multiples of i, so that i is always a multiple of j, regardless of what j is
        while j <= max_A :
            # If j is in the list of divisors, and i is not listed as a divisor of j, then add i as a divisor of j
            if j in divisors and i not in divisors[j] :
                divisors[j].append(i)
            j += i
        i += 1

    # The result for each number is the array length minus the total number of occurances of its divisors
    result = []
    for element in A:
        result.append(N-sum([occurances.get(div,0) for div in divisors[element]]))

    return result

""" Additional test input
    [3,4] - returned value = [1, 1]
    [10] - returned value = [0]
"""