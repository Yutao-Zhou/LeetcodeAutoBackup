class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        MAX_STRING = ''
        for i in range(len(s)):
            ## single
            tmp = self.checkPalindromic(s, i, i)
            print("%s-%s" % (str(i), tmp))
            if len(tmp) > len(MAX_STRING):
                MAX_STRING = tmp
            
            ## double
            tmp = self.checkPalindromic(s, i, i+1)
            if len(tmp) > len(MAX_STRING):
                MAX_STRING = tmp
        return MAX_STRING
        
    def checkPalindromic(self, s, l, r):
        while l >= 0 and r < len(s) and s[l]==s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
                
            
            
        
            
        