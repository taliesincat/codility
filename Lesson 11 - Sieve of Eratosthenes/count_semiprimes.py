""" CountSemiprimes
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N * log(log(N)) + M)
"""

def solution(N, P, Q):
    # Sieve of Eratosthenes
    sieve = [False]*2+[True]*(N-1)
    primes = list()
    prime_count = 0
    i = 2
    
    while i * i <= N:
        if sieve[i] == True :
            j = i * i
            primes.append(i)
            prime_count += 1
        while j <= N:
            sieve[j] = False
            j += i
        i += 1    
    
    while i <= N :
        if sieve[i] == True :
            primes.append(i)
            prime_count += 1
        i += 1
    
    # Calculate semiprimes from primes list.
    semiprime = [0] * (N + 1)

    for a in range(prime_count-1):
        for b in range(a, prime_count):
            if primes[a] * primes[b] > N:
                # So large that no need to record them.
                break
            # Mark semiprimes as 1    
            semiprime[primes[a] * primes[b]] = 1
    
    # Add up all semiprimes until index position.
    for k in range(1, N+1):
        semiprime[k] += semiprime[k-1]

    # Semiprimes between P[i] and Q[i] = semiprime[Q[i]] - semiprime[P[i] - 1].
    result = [0] * len(P)
    
    for k in range(len(P)):
        result[k] = semiprime[Q[k]] - semiprime[P[k]-1]
    
    return result