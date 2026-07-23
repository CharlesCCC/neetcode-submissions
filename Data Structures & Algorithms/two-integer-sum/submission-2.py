class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in prevMap:
                return [prevMap[need],i]
            prevMap[num] = i