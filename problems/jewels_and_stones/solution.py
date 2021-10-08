class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        counter = 0
        for i in jewels:
            for j in stones:
                if i == j:
                    counter += 1
                else:
                    pass
        return counter