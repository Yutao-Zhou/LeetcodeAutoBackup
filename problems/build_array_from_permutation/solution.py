class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0]*len(nums)
        i = 0
        for j in nums:
            ans[i] = nums[j]
            i += 1
        return ans