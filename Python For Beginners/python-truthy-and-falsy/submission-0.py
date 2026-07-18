def is_truthy(value) -> str:
    if type(value) is bool and value == False:
        return "Falsy"

    if value is None:
        return "Falsy"

    if value == 0 or value == 0.0:
        return "Falsy"

    if value:
        return "Truthy"
    else:
        return "Falsy"

    if value == []:
        return "Falsy"

    return "Truthy"



# don't modify code below this line
print(0, "is", is_truthy(0))
print(10, "is", is_truthy(10))

print(0.0, "is", is_truthy(0.0))
print(10.0, "is", is_truthy(10.0))

print("empty str", "is", is_truthy(""))
print("non-empty str", "is", is_truthy("non-empty str"))
