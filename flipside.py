# flipside
def flipside(s):
    
    """ takes in a string s and returns a string whose first half is s's second half and whose second half is s's first half."""
    # your code goes here
    string_length = len(s)
    middle = int(string_length/2)
    newstring = s[middle:]+s[:middle]
    return newstring

# Tests below, do not change
assert flipside('carpets') == 'petscar', f"Reported {flipside('carpets')} for flipside('carpets') instead of petscar"
assert flipside('homework') == 'workhome', f"Reported {flipside('homework')} for flipside('homework') instead of workhome"
assert flipside('ada') == 'daa', f"Reported {flipside('daa')} for flipside('ada') instead of daa"

# If the program gets here, the code works!
print("Your solution works!")