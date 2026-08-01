class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = "".join(char for char in s if char.isalnum()).lower()
        l,r= 0,len(string)-1
        while l < r :
            if string[l] != string[r]:
                return False
            else:
                l += 1
                r -= 1

        return True
        
