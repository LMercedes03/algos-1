# Compress

# Write a function, compress, that takes in a string as an argument. 
# The function should return a compressed version of the string where consecutive occurrences of 
# the same characters are compressed into the number of occurrences followed by the character. 
# Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'

# You can assume that the input only contains alphabetic characters.


def compress(s):
    compressed = ""
    count = 1
    n = len(s)

    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1
        else:
            if count > 1:
                compressed += str(count)
            compressed += s[i - 1]
            count = 1

    # Append the compressed representation of the last character(s) to the result
    if count > 1:
        compressed += str(count)
    compressed += s[-1]

    return compressed


# TEST CASES
result = compress('ccaaatsss') # -> '2c3at3s'
print(result)
# compress('ssssbbz') # -> '4s2bz'
# compress('ppoppppp') # -> '2po5p'
# compress('nnneeeeeeeeeeeezz') # -> '3n12e2z'
result = compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy');  # -> '127y'
print(result)
