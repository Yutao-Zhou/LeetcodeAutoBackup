class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = 0
        for i in nums:
            print(ans,i)
            if i < target:
                ans += 1
        return ans