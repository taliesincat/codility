""" Peaks
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N * log(log(N)))
"""

def solution(A):
    N = len(A)
    # Make array of peak positions. 0 means not a peak, 1 means peak
    peaks = [0] * N
    for i in range(1, N-1) :
        if A[i] > max(A[i+1], A[i-1]) :
            peaks[i] = 1

    # Can only have numbers of blocks that are factors of N.
    j = 1
    blocks = list()    
    while j <= N-1 :
        if N % j == 0:
            blocks.append(j)
        j += 1
    
    # Initialise
    max_blocks = 0
    
    # Iterate through list of potential numbers of blocks
    for k in blocks :
        # number of blocks = k:  length of each block is N/k
        block_count = 0
        length = int(N / k)
        start = 0
        end = length

        while end <= N :
            # If there's a peak present in this block, check the next block
            if 1 in peaks[start:end]:
                start += length
                end += length
                # If it's the last block of this set of length (N/k) blocks update block_count if k > block_count
                if end > N :
                    block_count = max(block_count, k)
            # If there's no peak present in this block, break out of the loop
            else :
                break
        # Update max number of blocks if block_count > max_blocks       
        max_blocks = max(max_blocks, block_count)
    
    return max_blocks

""" Additional test input
    [1,3,1] - returned value = 1
    [1,3,2,1] - returned value = 1
    [] - returned value = 0
    [3] - returned value = 0
"""