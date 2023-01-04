a = int(input("Enter num bw 5 and 10 "))

if a < 5 or a > 10:
    raise ValueError("Enter num bw 5 and 10")


b = input("Enter a string ")

if b != 'quit':
    raise ValueError("Enter quit")


class invalid_num(Exception):
    def __init__(self, msg="Enter num bw 1 and 10"):
        super().__init__(msg)


ip = int(input("Enter num bw 1 and 10 "))
if ip < 1 or ip > 10:
    raise invalid_num
