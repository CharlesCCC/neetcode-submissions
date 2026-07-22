from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    cm = defaultdict(int)
    for c in s:
        cm[c] += 1
    return cm


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    res = defaultdict(list)
    for nest_list in nums:
        key = nest_list[0];
        for index in range(1,len(nest_list)):
            res[key].append(nest_list[index])
    return res


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
