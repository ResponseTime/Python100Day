from datetime import datetime
b = datetime.now()
a = b.strftime("%H:%M:%S")
print(a)
if a >= "00:00:00" and a < "12:00:00":
    print("Good moring!")
elif a >= "12:00:00" and a <= "16:00:00":
    print("Good noon!")
elif a >= "17:00:00" and a <= "21:00:00":
    print("Good evening!")
elif a > "21:00:00" and a <= "23:59:59":
    print("Good night!")
