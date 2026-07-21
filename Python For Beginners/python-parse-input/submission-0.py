from typing import List

def read_integers() -> List[int]:
    ui = str(input()) 
    strlist = ui.split(",")
    res = []
    for s in strlist:
        res.append(int(s))
    return res

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
