class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
#         for i in range(len(nums)):
#             difference=target-nums[i]
#             if ((difference in nums) and (difference==nums[1])):
#                 return[i,1]
#             elif ((difference in nums) and (difference!= nums[i])):
                
#                 return[i,nums.index(difference)]
        
        NumsMap = dict()
        for i in range(len(nums)):
            num = nums[i]
            diff = target-num
            if diff in NumsMap:
                return [i, NumsMap[diff]] # find if difference exists
            else:
                NumsMap[num] = i # map num to idx
                
                
                
            
            