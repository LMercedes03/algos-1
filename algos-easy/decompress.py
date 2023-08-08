# Decompress

# Write a function, decompress, that takes in a string as an argument. 
# The input string will be formatted into multiple groups according to the following pattern:

# <number><char>
# for example, '2c' or '3a'.

# The function should return an decompressed version of the string where each 'char' of a group 
# is repeated 'number' times consecutively. 
# You may assume that the input string is well-formed according to the previously mentioned pattern.

def decompress(s):
    result = ""
    i = 0  # tracks the character
 
    # while i < len(s):
    #     count = int(s[i])  # Get the number
    #     char = s[i + 1]  # Get the character
    #     result += count * char # Repeat the character count number of times
    #     i += 2  # Move to the next group
    #     print(result)

    while i < len(s):
        count_str = ""
        while i < len(s) and s[i].isdigit():
            count_str += s[i]  # Accumulate the digit characters to form the count string
            i += 1
        count = int(count_str)  # Convert the count string to an integer
        char = s[i]  # Get the character
        result += char * count  # Repeat the character count number of times consecutively
        i += 1  # Move to the next group
    return result



# TEST CASES
decompress("2c3a1t") # -> 'ccaaat'
decompress("4s2b") # -> 'ssssbb'
decompress("2p1o5p") # -> 'ppoppppp'
decompress("3n12e2z") # -> 'nnneeeeeeeeeeeezz'
decompress("127y") # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
