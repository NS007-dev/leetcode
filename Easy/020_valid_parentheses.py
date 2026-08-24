# 20. Valid Parentheses
# Easy
# Topics
# premium lock iconCompanies
# Hint

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

 

# Constraints:

#     1 <= s.length <= 104
#     s consists of parentheses only '()[]{}'.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                # Pop top element if stack not empty, else assign dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check popped bracket matches expected opening bracket
                if mapping[char] != top_element:
                    return False
            else:
                # It's opening bracket, push it to the stack
                stack.append(char)

        # If stack empty, all brackets were properly matched
        return not stack

