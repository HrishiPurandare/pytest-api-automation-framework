def only_in_a(A, B):
    """
    Problem B:
    Compare two arrays A and B and return elements that are in A but not in B.
    - Preserves the original order of A.
    - Keeps duplicates from A if they are not present in B.
    
    Parameters:
    - A: list of any hashable elements
    - B: list of any hashable elements
    
    Returns:
    - A new list containing elements from A that are not in B
    """
    # Convert B to a set for fast membership checks (average-case O(1) lookups)
    b_set = set(B)

    # Build the result by including x from A only if x is not in B
    # This preserves the order of A and retains duplicates from A
    return [x for x in A if x not in b_set]


# Example from the problem statement
A = [11, 22, 32, 42]
B = [2, 4, 6]

output = only_in_a(A, B)
print(output)  # Expected: [1, 3]
