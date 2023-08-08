# Paired Parentheses

# Write a function, paired_parens, that takes in a string as an argument. 
# The function should return a boolean indicating whether or not the string has well-formed parentheses.
# You may assume the string contains only alphabetic characters, '(', or ')'.


def paired_parens(string):

# Define opening and closing parenthesis and create a list to store the occurences of parenthesis
  open = "("
  close = ")"
  parensList = []

  for char in string:
    # Char is equal to "(" append to parensList
    if char == open:
      parensList.append(char)
  
    # Else if current char is equal to ")" and  remove the top element of list
    elif char == close:
      if not parensList:
        return False
      parensList.pop()

  # Check if parensList is empty. If empty all opening parentheses have been matched and removed.
  return len(parensList) == 0




# Define opening and closing parenthesis
  # open = "("
  # close = ")"
  # count1 = 0
  # count2= 0

# We need to iterate through the given string and check if opening parens are 
# equal to closing parens to determine if they are well formed

  # for char in string:
  #   if char == open:
  #     count1 += 1 
  #   if char == close:
  #     count2 += 1

  # if count1 == count2:
  #   return True
  # else:
  #   return False
      


# TEST CASES
result = paired_parens("(david)((abby))") # -> True
print(result)
result = paired_parens("()rose(jeff") # -> False
print(result)
result = paired_parens(")(") # -> False
print(result)
result = paired_parens("()") # -> True
print(result)
result = paired_parens("(((potato())))") # -> True
print(result)
result = paired_parens("(())(water)()") # -> True
print(result)