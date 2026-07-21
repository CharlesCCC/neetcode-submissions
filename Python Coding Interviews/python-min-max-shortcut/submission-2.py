from typing import List


def disallow_negatives(num: int) -> int:
    return max(0,num)


def max_difference(nums: List[int]) -> int:
    res = 0
    # zip pairs nums[0] with nums[1], nums[1] with nums[2], etc.
    for prev, curr in zip(nums,nums[1:]): # fix the range - pythonic way
        res = max(res, curr - prev)
    
    return res


# do not modify below this line
print(disallow_negatives(-2))
print(disallow_negatives(-1))
print(disallow_negatives(0))
print(disallow_negatives(1))
print(disallow_negatives(2))

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_difference([1, 2, 3, 4, 5, 6, 8, 9]))
print(max_difference([10, 1, 3, 7]))
print(max_difference([2, 4, 7, 5, 7, 8, 4, 2]))
