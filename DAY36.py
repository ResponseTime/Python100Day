try:
    a = int(input("Enter num : "))
    for i in range(1, 11):
        print("{} * {} = {}".format(a, i, a*i))
except Exception as e:
    print("Invalid input {}".format(e))

try:
    a = int(input("Enter num : "))
    ls = [32, 465, 7]
    print(ls[a])
except IndexError:
    print("Invalid index")
