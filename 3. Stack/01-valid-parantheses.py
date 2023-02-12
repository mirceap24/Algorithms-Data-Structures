# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Input: s = "()"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        # stack to keep track of opening brackets
        stack = []

        # Hash map for keeping track of mappings
        mapping = {")": "(", "}": "{", "]": "["}

        # for every bracket in expression 
        for char in s:
            # if char is a closing bracket
            if char in mapping:
                # pop the topmost element from the stack if it's non empty
                # assign a value to the top_element if stack is empty
                top_element = stack.pop() if stack else "!"
                # the mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False 
            else:
                # opening bracket, push onto the stack
                stack.append(char)
        
        return not stack