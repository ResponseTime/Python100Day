print("Calculator")
result = 0
print("Enter nums")
a = int(input())
b = int(input())
choose = input("Enter + - * /")
if choose == '+':
    result = a+b
elif choose == '-':
    result = a-b
elif choose == '*':
    result = a*b
elif choose == '/':
    result = a//b

print(result)
