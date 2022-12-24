# import random
# s = "naming"
# # k = ''.join(random.sample(s,len(s)))
# k = []
# while len(k) != len(s):
#     j = random.choice(s)
#     if k.count(j) == s.count(j):
#         continue
#     k.append(j)


# print(k)
prize = 0
print("KBC ")
while True:
    print("Q1 for 1000rs")
    print("What is my name")
    print(['aayush', 'looper', 'renegade', 'Ni...'])
    ans = input("Enter your answer: ").lower()
    if ans == 'aayush':
        prize += 1000
        print("Correct answer")
        print(f"Your prize is {prize}")
    else:
        print("Wrong answer")
        print(f"Your prize is {prize}")
        break
    print("Q2 for 2000rs")
    print(" what is my age ")
    print(['18', '19', '20', '21'])
    ans = input("Enter your answer: ").lower()
    if ans == '20':
        prize += 2000
        print("Correct answer")
        print(f"Your prize is {prize}")
    else:
        print("Wrong answer")
        print(f"Your prize is {prize}")
        break
    print("Q3 for 3000rs")
    print(" what is my fav color ")
    print(['red', 'blue', 'green', 'yellow'])
    ans = input("Enter your answer: ").lower()
    if ans == 'red':
        prize += 3000
        print("Correct answer")
        print(f"Your prize is {prize}")
    else:
        print("Wrong answer")
        print(f"Your prize is {prize}")
        break
    print("Q4 for 4000rs")
    print(" what is my fav food ")
    print(['burger', 'pizza', 'pasta', 'chicken'])
    ans = input("Enter your answer: ").lower()
    if ans == 'burger':
        prize += 4000
        print("Correct answer")
        print(f"Your prize is {prize}")
    else:
        print("Wrong answer")
        print(f"Your prize is {prize}")
        break
    if prize == 10000:
        print("You won the game")
        break
