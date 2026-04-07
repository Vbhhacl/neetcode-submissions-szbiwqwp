class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = ''.join(char for char in s if char.isalnum()).lower()
        str2 = str1[::-1]
        if str2==str1:
            return True
        return False