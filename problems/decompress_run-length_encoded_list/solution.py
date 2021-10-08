class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        i = 0
        while i < len(nums):
            if (i % 2) == 0:
                ans.append([nums[i+1]]*nums[i])
                i += 2
        ans = sum(ans, [])
        return ans