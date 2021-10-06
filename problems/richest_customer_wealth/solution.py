class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        ans=[]
        for i in range(len(accounts)):
            ans.append(sum(accounts[i]))
        return max(ans)