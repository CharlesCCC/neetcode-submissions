class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = set()
        nums.sort()
        count = defaultdict(int)

        for num in nums:
            count[num] += 1;
        
        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                #skip duplicate
                continue
            
            for j in range(i+1, len(nums)):
                count[nums[j]] -= 1;
                if j - 1 > i and nums[j] == nums[j-1]:
                    #skip 
                    continue
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i],nums[j],target])
            for j in range(i + 1, len(nums)):
                count[nums[j]] +=1
            
        return res
            