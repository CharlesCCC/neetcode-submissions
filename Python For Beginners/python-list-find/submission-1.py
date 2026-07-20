from typing import List # this is used to add type hints for List type

def find_index(nums: List[int], target: int) -> int:
    index = -1 
    for n in nums:
        index += 1
        if n == target:
            return index
    return index 


# don't modify code below this line
print(find_index([1, 2, 3, 4, 5], 3))
print(find_index([1, 2, 3, 4, 5, 3], 3))
print(find_index([1, 2, 3, 4], 1))
print(find_index([1, 3, 4, 2], 2))

