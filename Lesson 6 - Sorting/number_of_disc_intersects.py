""" NumberOfDiscIntersections
    
    Task score: 100%
    Correctness: 100%
    Performance: 100%
    Detected time complexity: O(N*log(N)) or O(N)
"""

def solution(A):    
    edges = list() # Edges of circles on the axis
    for x, y in enumerate(A):
        # Store as tuple; point on x axis and whether it's a left- or right-hand edge
        # Mark left-hand edge points as 0, right-hand edge points as 1
        edges += [(x-y, 0), (x+y, 1)]        
    edges.sort() # Sort edges by smaller point on axis.
    
    # Initiate number of intersections and number of active circles
    intersections = 0
    circles = 0

    for i, j in edges:        
        if j == 0 : # If the edge is a right-hand edge            
            intersections += circles # Add number of active circles to number of intersections.
            circles += 1 # Increase number of active circles by 1.
        else :
            circles -= 1 # Decrease number of active circles by 1
        # Return -1 if the number of intersecting pairs exceeds 10,000,000
        if intersections > 10000000 :
            return -1

    return intersections
