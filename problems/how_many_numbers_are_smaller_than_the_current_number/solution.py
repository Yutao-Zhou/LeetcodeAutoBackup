class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        counter = 0
        for j in range(len(nums)):
            for i in nums:
                if i < nums[j]:
                    counter += 1
                else:
                    pass
            ans.append(counter)
            counter = 0
        return ans