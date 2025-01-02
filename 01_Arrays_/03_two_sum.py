class Solution:
    def twoSum(self , nums , target):
            
        maps = {}
        for i , num in enumerate(nums):
            if target - num in maps:

                return [i , maps[target - num]]
            maps[num] = i 
        return 