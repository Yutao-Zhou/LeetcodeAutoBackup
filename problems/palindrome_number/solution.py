class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = list(map(str,str(x)))
        if len(x) == 1:
            return True
        for i in range(len(x)/2):
            if x[i] == x[-i-1]:
                pass
            else:
                return False
        return True