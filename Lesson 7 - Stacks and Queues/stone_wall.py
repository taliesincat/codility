""" StoneWall
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N)
"""

def solution(H):
    N = len(H)
    blocks = list() #Stack of blocks
    count = 0 # Block counter

    for i in range(N) :
        # If there are no blocks in the stack, add the height of the current block to the stack
        if len(blocks) == 0:
            blocks.append(H[i])

        # If the next piece of wall is shorter than the last block in the stack, remove block from the stack, add one to counter, until there are either no blocks in the stack
        # or the next block is the same height or taller height or taller as the next piece of wall.
        if H[i] < blocks[-1] : 
            while H[i] < blocks[-1] and len(blocks) > 1:
                blocks.pop()
                count += 1
            # If the current piece of wall is the same height as the last block in the stack, don't append to stack, otherwise do.
            if len(blocks) != 0 and H[i] == blocks[-1]:
                continue
            else:
                blocks.append(H[i])
        
        # If the next piece of wall is taller than the last block in the stack, add to stack.
        if H[i] > blocks[-1] :
            blocks.append(H[i])       
  
    # Total number of blocks is the counter plus however many are left in the stack at the end of array H.
    count += len(blocks)
    return count

""" Additional test input
    [8,9,8,9,8,9,8,9,8] - returned value = 5
    [10,1,2,3,4,5,6,7,8,9,1] - returned value = 10
    [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1] - returned value = 9
"""


