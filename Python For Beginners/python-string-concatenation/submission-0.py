def concatenate(s1: str, s2: str) -> str:
    res = s1 + s2
    if len(res) > 10:
        return "Too long!"
    else:
        return res




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
