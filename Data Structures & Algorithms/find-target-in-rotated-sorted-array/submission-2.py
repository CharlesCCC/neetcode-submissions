class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: 
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid 
            
            if nums[l] <= nums[mid]: # 1（l) 2 3(mid) 4 X X X(r)
                # on left sorted portion , check two edge/boundries 
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:  #4(l),5, 1(mid),2, X X X(r)
                # on right sorted portion, check two edge/boundries 
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1 
                else:
                    l = mid + 1
        return -1