a = input("Enter a number ")
a = list(a)

for i in a:
    try:
        i = int(i)
    except ValueError:
        print("Invalid number")
        break
    match i:
        case 0:
            print("Zero", end=" ")
        case 1:
            print("One", end=" ")
        case 2:
            print("Two", end=" ")
        case 3:
            print("Three", end=" ")
        case 4:
            print("Four", end=" ")
        case 5:
            print("Five", end=" ")
        case 6:
            print("Six", end=" ")
        case 7:
            print("Seven", end=" ")
        case 8:
            print("Eight", end=" ")
        case 9:
            print("Nine", end=" ")
        case _:
            print("Enter a valid number")
