""" CommonPrimeDivisors
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(Z * log(max(A) + max(B))**2)
"""

# Function to find greatest common divisor
def greatest_common_divisor(a, b):
    if a % b == 0:
        return b
    else:
        return greatest_common_divisor(b, a % b)

def solution(A, B):
    count = 0
    # Find greatest common divisor between A[i] and B[i]
    for i in range(len(A)):
        a, b = A[i], B[i]
        gcd = greatest_common_divisor(a, b)
        while True :
            # Find greatest common divisor between the greatest common divisor and A[i]
            divisor1 = greatest_common_divisor(a, gcd)
            if divisor1 == 1 :
                break
            a /= divisor1
        while True:
            # Find greatest common divisor between the greatest common divisor
            # and B[i]
            divisor2 = greatest_common_divisor(b, gcd)
            if divisor2 == 1 :
                break
            b /= divisor2
        # If they have the same common divisors, increment count
        if a == 1 and b == 1 :
            count += 1

    return count
