import time as t
import getpass


class User():
    Username = None
    Password = None

    def __init__(self):
        file = open('details.txt', 'a')
        file.close()

    def signup(self):
        val = input("Enter username ")
        val2 = getpass.getpass()
        self.Username = val
        self.Password = val2
        with open('details.txt', 'a') as detail:
            detail.writelines(self.Username+":"+self.Password)
            detail.write('\n')

    def login(self):
        while True:
            val = input("Enter username ")
            val2 = getpass.getpass()
            with open('details.txt', 'r') as details:
                data_obj = []
                for i in details.readlines():
                    data_obj.append(i.rstrip('\n'))
                if f"{val}:{val2}" in data_obj:
                    break
                else:
                    print("Invalid username or password ")
                    value = input("To sign up enter 0 ")
                    if value == '0':
                        self.signup()


print("Enter exit() to exit the terminal")
User = User()
User.login()
while True:
    val = input("$ ")
    if val == 'exit()':
        break
    t.sleep(0.2)
