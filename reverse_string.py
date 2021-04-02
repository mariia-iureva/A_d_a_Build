def reverse_string(input_str):
    answer = ""
    # Your code goes here
    string_length = len(input_str)
    i = 1
    for letter in input_str:
      while i <= string_length:
        answer += input_str[-i]
        i+=1

    #  End of your code
    return answer

# Tests below, do not change
assert reverse_string("hello") == "olleh", "Cannot reverse 'hello'"
assert reverse_string("") == "", "When given an empty string it returns an empty string, but doesn't"
assert reverse_string("racecar") == "racecar", "Cannot reverse 'racecar'"
assert reverse_string("12345") == "54321", "Cannot reverse 12345"

# If the program gets here, the code works!
print("Your solution works!")
