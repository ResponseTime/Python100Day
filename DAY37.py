try:
    ls = [32, 54, 7, 232]
    print(ls[int(input("Enter the index: "))])
except IndexError:
    print("Index out of range")
finally:
    print("Always executed")


def func():
    try:
        ls = [32, 54, 7, 232]
        print(ls[int(input("Enter the index: "))])
        return 1
    except IndexError:
        print("Index out of range")
        return 0
    finally:
        print("Always executed")


cx = func()
print(cx)
