""" MaxCounters
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N + M)
"""

def solution(N, A):
    counters = [0] * N # List to be returned.
    max_counter = 0 # Value in previous max_counter commands.
    current_max = 0 # The current maximum value of counter.

    for num in A:
        if 1 <= num <= N : # Operation K is increase(X).            
            if max_counter > counters[num-1]:
                counters[num-1] = max_counter # Update max_counter to the number at the end of the list.
            counters[num-1] += 1 # Increase the last number in the counters list.
            if current_max < counters[num-1]:
                current_max = counters[num-1] # Update current_max to the number at the end of the list.
        else: # Operation K is max_counter.
            max_counter = current_max # Update max_counter to the current maximum value.
        
    for i in range(0,N):
        if counters[i] < max_counter:
            counters[i] = max_counter # Update list before returning it.

    return counters

""" Additional test input
    (4, [-1, 1, 2, 5, 6, 4, 8]) - returned value = [2, 2, 2, 2]
    (9, [-1, 1, 2, 5, -6, 4, 8, 4, 10, -5]) - returned value = [3, 3, 3, 3, 3, 3, 3, 3, 3]
    (1, [1]) - returned value = [1]
    (2, [2]) - returned value = [0, 1]
    (5, [6, 3, 4, 4, 6, 1, 4, 4]) - returned value = [3, 2, 2, 4, 2]
    (5, [6, 3, 7, 4, 4, 6, 1, 4, 4]) - returned value = [4, 3, 3, 5, 3]
    (5, [6, 3, -7, 4, 4, 6, 1, 4, 4]) - returned value = [4, 3, 3, 5, 3]
    (5, [6, -3, -7, 4, 4, 6, 1, 4, 4]) - returned value = [3, 2, 2, 4, 2]
    (10, [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]) - returned value = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
"""
