l = [23, 7, 'hello world', 5.67, (24, 67, 89), [1, 2, 3], {1, 2, 3}, {
    'name': 'John', 'age': 23}]
print(type(l[6]))

print({1, 2, 3} in l)
print((l[5:6]))
print(l[::2])

lst = [i*i for i in range(6)]
print(lst)

names = ['milo', 'jane', 'john', 'jane', 'jane']
na = [i for i in names if i.endswith('e') or i.endswith('n')]
print(na)
