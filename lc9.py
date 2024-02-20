# Palindrome Number:
# Given an integer x, return true if x is a 
palindrome
, and false otherwise
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        orig = x
        reverse = 0
        remainder = 0
        
        while x >= 10:
            remainder = x % 10
            x = x // 10
            reverse += remainder
            reverse *= 10
        reverse += x
        if reverse == orig:
            return True
        return False
        
