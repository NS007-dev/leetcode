# 5. Longest Palindromic Substring
# Medium
# Topics
# premium lock iconCompanies
# Hint

# Given a string s, return the longest in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"

 

# Constraints:

#     1 <= s.length <= 1000
#     s consist of only digits and English letters.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        start, max_len = 0, 0

        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # length
            return right - left - 1

        for i in range(len(s)):
            # odd, single
            len1 = expand_around_center(i, i)
            # even, 2 char
            len2 = expand_around_center(i, i + 1)
            
            length = max(len1, len2)

            if length > max_len:
                max_len = length
                # index
                start = i - (length - 1) // 2

        return s[start : start + max_len]