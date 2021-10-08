class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        j = 0
        ans = []
        for i in index:
            ans.insert(i, nums[j])
            j += 1
        return ans