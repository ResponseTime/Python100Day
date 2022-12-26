def my_func(*args):
    '''Function that returns the avg of the arguments passed'''
    return sum(args)/len(args)


print(my_func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(my_func.__doc__)
print(help(my_func))


# pep8 DAY29.py
