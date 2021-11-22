class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ###### bad solution ####
#         cach1 = 0
#         cach2 = 0
#         cach3 = 0
#         for i in nums:
#             print(cach1,cach2,cach3)
#             if i > cach1:
#                 cach1 = i
#             elif i > cach2:
#                 cach2 = i
#             elif i > cach3:
#                 cach3 = i
        
#         if len(set(nums)) < 3:
#             return cach1
#         else:
#             return cach3
        
        ###### set #######
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        print(nums)
        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]