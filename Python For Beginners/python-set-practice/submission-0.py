from typing import List

def contains_duplicate(words: List[str]) -> bool:
    origin_n = len(words)
    new_n = len(set(words))
    if origin_n == new_n:
        return False
    else:
        return True

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
