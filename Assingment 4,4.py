# Define a function named odd_values_string that takes one argument, 'str'.
def odd_values_string(str):
    # Initialize an empty string 'result' to store characters with odd indices.
    result = ""
    
    # Iterate through the indices (i) of the characters in the input string 'str'.
    for i in range(len(str)):
        # Check if the index (i) is even (i.e., has a remainder of 0 when divided by 2).
        if i % 2 == 0:
            # If the index is even, append the character at that index to the 'result' string.
            result = result + str[i]
    
    # Return the 'result' string containing characters with odd indices.
    return result

# Call the odd_values_string function with different input strings and print the results.
print(odd_values_string('abcdef'))  # Output: 'ace'
print(odd_values_string('python'))  # Output: 'pto'
