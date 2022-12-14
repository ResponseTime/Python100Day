import time
name = "aayush"
for i in name:
    print(i.upper(), end=" ")

dict2 = {
    "name": "aayush",
    "age": 20,
    "salary": 300000
}

print()
for i, j in dict2.items():
    print(j, i)

lst = [23, 65, 87, 233, 545]

for i, j in enumerate(lst):
    print(i, j)

# for i in range(200000):
#     print(i)

for i in range(0, 7, 2):
    print(i)
