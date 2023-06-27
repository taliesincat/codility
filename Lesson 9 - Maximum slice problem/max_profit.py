""" MaxProfit
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N)
"""

def solution(A):
    N = len(A)
    # If there are no days passing then there is no profit
    if N <= 1 :
        return 0

    # Initialise buy_day and sell_day as the start of the array
    buy_day = A[0]
    sell_day = A[0]
    max_profit = 0

    for i in range(N):
        # If today's value is less than buy_day, update buy_day
        if buy_day < A[i] :
            buy_day = A[i]
        # If sell_day is greater than today's value, update buy_day and sell_day to today
        if sell_day > A[i] :
            buy_day = A[i]
            sell_day = A[i]

        # Update max_profit if applicable 
        if max_profit < (buy_day - sell_day) :
            max_profit = buy_day - sell_day

    return max_profit

""" Additional test input
    [4,5,6,9,1,10] - returned value = 9
    [1,2,3,4,5,6,7,8,9,1,3] - returned value = 8
    [] - returned value = 0
    [1] - returned value = 0
    [1,100] - returned value = 99
"""