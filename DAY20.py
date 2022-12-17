def gmean(a: int, b: int) -> float:
    return (a*b)/(a+b)


def is_greater(a: int, b: int) -> bool:
    return a > b


print(gmean(4, 6))
print(gmean(43, 26))
print(gmean(9, 8))
print(is_greater(4, 6))
