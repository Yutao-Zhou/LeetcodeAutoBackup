class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        counter = 0
        if num == 0:
            return 0
        while num > 0:
            if (num % 2) == 0:
                num /= 2
                counter += 1
            elif num == 1 :
                counter += 1
                return counter
            else:
                num -= 1
                counter +=1