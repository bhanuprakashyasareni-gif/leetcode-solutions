class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l , r = 0 ,0
        if len(s) == 0 and len(t) == 0 :
            return True
        elif len(s) == 0 :
            return True
        elif len(s) > len(t):
            return False
        while l < len(t):
            if s[r] == t[l]:
                r+= 1
                l+= 1
                if len(s) == r :
                    return True
            else:
                l += 1
        return False
        
