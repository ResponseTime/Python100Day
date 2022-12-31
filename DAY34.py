s1 = {'name': 'test1', 'age': 20}
s2 = {'name': 'test2', 'age': 30}
# s1.update(s2)
print(s1.pop('name'))
print(s1.popitem())
s1.clear()
del s2['age']
print(s2)
