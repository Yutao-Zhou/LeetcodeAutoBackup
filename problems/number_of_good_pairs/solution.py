
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=[]
        check=[]
        i=0
        for i in range(len(nums)):
                if nums[i] in check:
                    pass
                else:
                    check.append(nums[i])
                    a=nums.count(nums[i])
                    y=a*(a-1)//2
                    ans.append(y)
        return sum(ans)