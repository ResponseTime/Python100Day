s1 = {43, 76, 99, 1011}
s2 = {56, 34, 76, 43, 2}

print(s1.union(s2))
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.intersection(s2))
s1.update(s2)
print(s1.symmetric_difference(s2))
print(s1.issubset(s2))
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
s1.add(23)
s1.remove(1011)
print(s1)
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1)
del s2
print(s2)
s1.clear()
