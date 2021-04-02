# triple - complete solution.
def triple(n): # Fix this function.
    """
    input: integer or float n
    output: three times the input
    """
    return 3 * n

# Tests below, do not change
assert triple(3) == 9, f"Reported {triple(3)} for triple(3) instead of 9"
assert triple(-3) == -9, f"Reported {triple(-3)} for triple(-3) instead of -9"
assert triple(1.5) == 4.5, f"Reported {triple(1.5)} for triple(1.5) instead of 4.5"

# If the program gets here, the code works!
print("Your solution works!")