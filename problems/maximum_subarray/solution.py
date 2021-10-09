class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        counts = 0
        max_ = -10001
        for i, num in enumerate(nums):
            if i == 0:
                counts = num
            else:
                counts = max(num, counts + num)
            max_ = max(counts, max_)
        return max_