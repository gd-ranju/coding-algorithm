# Time Complexity: O(n), where n is the number of elements in nums.
# We iterate over the list once and each lookup/insertion operation in the dictionary takes constant time on average.

# Space Complexity: O(n), where n is the number of elements in nums.
# The dictionary 'prevMap' stores at most n elements in the worst case, corresponding to the number of numbers in the list.



class Solution:
    def twoSum(self, nums, target: int) -> list[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
