# Anagrams

# Write a function, anagrams, that takes in two strings as arguments. 
# The function should return a boolean indicating whether or not the strings are anagrams. 
# Anagrams are strings that contain the same characters, but in any order.

def anagrams(s1, s2):
    # Compare if the length of strings are equal. If not return false.
    if len(s1) != len(s2):
        return False

    # Initialize two empty dictionaries to hold character count for each string.
    # Iterate through each string and count the frequency of each character.
    count1 = {}
    count2 = {}

    for char in s1:
        count1[char] = count1.get(char, 0) + 1
    for char in s2:
        count2[char] = count2.get(char, 0) + 1

    # Compare the character frequencies if equal return true else return false
    return count1 == count2


# # TEST CASES
result = anagrams('restful', 'fluster')  # -> True
print(result)
result2 = anagrams('cats', 'tocs')  # -> False
print(result2)
# anagrams('monkeyswrite', 'newyorktimes') # -> True
# anagrams('paper', 'reapa') # -> False
# anagrams('elbow', 'below') # -> True
# anagrams('tax', 'taxi') # -> False
# anagrams('taxi', 'tax') # -> False
# anagrams('night', 'thing') # -> True
# anagrams('po', 'popp') # -> False
# anagrams('pp', 'oo') # -> False
