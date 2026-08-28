# 7. Reverse Integer
# Medium
# Topics
# premium lock iconCompanies

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321

# Example 2:

# Input: x = -123
# Output: -321

# Example 3:

# Input: x = 120
# Output: 21

 

# Constraints:

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #sign
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Reverse digits  string manip
        reversed_x = int(str(x)[::-1]) * sign

        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0

        return reversed_x