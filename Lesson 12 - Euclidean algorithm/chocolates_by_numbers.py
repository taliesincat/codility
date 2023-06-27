""" ChocolatesByNumbers
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(log(N + M))
"""

# Number of chocolates that can be eaten is the least common multiple of N and K, where K is the greatest common divisor of N and M.
# Least common multiple of N and K is the smallest positive integer that is divisible by both N and K

def greatest_common_divisor(A, B):
    if A % B == 0:
        return B
    else:
        return greatest_common_divisor(B, A % B)

def solution(N, M):
    K = greatest_common_divisor(N, M)
    lcm = N / K
    chocolates = int(lcm)
    return chocolates

""" Additional test input
    10, 5 - returned value = 2
    69, 3 - returned value = 23
    3, 69 - returned value = 1
    1, 50 - returned value = 1
"""