class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        i = 0
        l = len(nums)
        while i < (len(nums)-1):
            if nums[i] == nums[i+1] and l != 2:
                nums.pop(i)
                k += 1
            elif nums[i] == nums[i+1] and l == 2:
                nums.pop(i)
                k += 1
                i += 1
            else:
                i += 1
                pass