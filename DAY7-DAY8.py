print("Calculator")
result = 0

while True:
    ch = input("Enter operator ")
    if ch == '...':
        break
    if result == 0:
        val = int(input("Enter num "))
        val2 = int(input("Enter num  "))
        if ch == '+':
            result = val + val2
        elif ch == '/':
            result = val / val2
        elif ch == '-':
            result = val - val2
        elif ch == '*':
            result = val + val2
        else:
            print("wrong operator")
    else:
        val3 = int(input("Enter num "))
        if ch == '+':
            result += val3
        elif ch == '/':
            result /= val3
        elif ch == '-':
            result -= val3
        elif ch == '*':
            result *= val3
        else:
            print("wrong operator")
    print("Ans is ", result)
