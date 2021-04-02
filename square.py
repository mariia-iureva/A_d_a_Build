# square
def square(n):
    """
    input: an integer or float value n
    output: the square of n (n*n)
    """
    
    return n**2 # your code goes here

# Tests below, do not change
assert square(3) == 9, f"Reported {square(3)} for square(3) instead of 9"
assert square(-3) == 9, f"Reported {square(-3)} for square(-3) instead of 9"

# If the program gets here, the code works!
print("Your solution works!")