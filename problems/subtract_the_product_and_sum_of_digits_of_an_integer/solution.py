class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(n)
        n = list(n)
        n = map(int, n)
        mul = 1
        add = sum(n)
        for i in range(len(n)):
            mul *= n[i]
        ans = mul - add
        return ans