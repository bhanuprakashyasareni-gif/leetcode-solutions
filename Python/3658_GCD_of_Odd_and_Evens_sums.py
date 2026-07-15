class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        return gcd(n*n , n*(n+1))
        
