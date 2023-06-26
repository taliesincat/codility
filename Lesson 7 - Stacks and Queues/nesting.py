""" Nesting
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N)
"""

def solution(S):
    N = len(S)
    # If there are an odd number of characters in the string then it can't be properly nested
    if N % 2 != 0:
        return 0
    
    stack = list()

    for bracket in S :        
        if bracket == '(' :
            # If it's an open bracket, add to the stack
            stack.append(bracket)
        else:            
            if len(stack) == 0 :
                # If there's nothing in the stack, return 0
                return 0            
            else:
                # Else bracket must be a close bracket: pop the last open bracket added to the stack off
                stack.pop()

    # If the stack is empty after the for loop, S is a properly nested string.
    # If there are things in the stack still, S is not a properly nested string.
    if len(stack) == 0 :
        return 1
    else:
        return 0
    
""" Additional test input
    '()' - returned value = 1
    '())' - returned value = 0
    '((((((((()))))))' - returned value = 0
    ')(' - returned value = 0
    '()())(()()' - returned value = 0
"""