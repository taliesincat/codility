""" Brackets
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N)
"""

def solution(S):
    N = len(S)
    # If there are an odd number of characters in the string then it can't be properly nested
    if N % 2 != 0 :
        return 0

    stack = list()
    open_bracket = ['[', '{', '(']
    
    for bracket in S:        
        if bracket in open_bracket:
            stack.append(bracket) # If it's an open bracket, add to the stack
        else:
            # If there's current nothing in the stack (and the bracket isn't an open bracket), it's not a nested string, so return 0.
            if len(stack) == 0:
                return 0
            # If it's a close bracket that is the opposite of the last bracket added to the stack, pop the last bracket added to the stack off.
            elif bracket == ']' and stack[-1] == '[' :
                stack.pop()                
            elif bracket == '}' and stack[-1] == '{' :
                stack.pop()
            elif bracket == ')' and stack[-1] == '(' :
                stack.pop()
    
    # If the stack is empty after the for loop, S is a properly nested string.
    # If there are things in the stack still, S is not a properly nested string.
    if len(stack) == 0:
        return 1
    else :
        return 0
    
""" Additional test input
    '([)()]' - returned value = 0
    '()[]{}' - returned value = 1
    '(()[{(}])' - returned value = 0
    '(()[{(]}])' - returned value = 0
    '((((((((()))))))' - returned value = 0
    ')(' - returned value = 0
    '()())(()()' - returned value = 0
"""