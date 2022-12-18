def avg(a=1, b=1):
    return (a + b) / 2


def avgg(*args):
    return sum(args) / len(args)


def makeDict(**kwargs):
    for i, j in kwargs.items():
        print(i, j)


print(avg(1, 2))
print(avg(3))
print(avg(b=4))


print(avgg(2, 3, 4, 5, 6, 7, 8, 9, 10))

makeDict(a=1, b=2, c=3, d=4, e=5)
