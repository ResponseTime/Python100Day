# # import time as t
# # import getpass


# # class User():
# #     Username = None
# #     Password = None

# #     def __init__(self):
# #         file = open('details.txt', 'a')
# #         file.close()

# #     def signup(self):
# #         val = input("Enter username ")
# #         val2 = getpass.getpass()
# #         self.Username = val
# #         self.Password = val2
# #         with open('details.txt', 'a') as detail:
# #             detail.writelines(self.Username+":"+self.Password)
# #             detail.write('\n')

# #     def login(self):
# #         while True:
# #             val = input("Enter username ")
# #             val2 = getpass.getpass()
# #             with open('details.txt', 'r') as details:
# #                 data_obj = []
# #                 for i in details.readlines():
# #                     data_obj.append(i.rstrip('\n'))
# #                 if f"{val}:{val2}" in data_obj:
# #                     break
# #                 else:
# #                     print("Invalid username or password ")
# #                     value = input("To sign up enter 0 ")
# #                     if value == '0':
# #                         self.signup()


# # print("Enter exit() to exit the terminal")
# # User = User()
# # User.login()
# # while True:
# #     val = input("$ ")
# #     if val == 'exit()':
# #         break
# #     t.sleep(0.2)
# import tkinter as tk

# class App:
#     def __init__(self, root):
#         # Create a label to display the input
#         self.label = tk.Label(root, text="")
#         self.label.pack()

#         # Create a text entry box for the user to input
#         self.entry = tk.Entry(root)
#         self.entry.pack()

#         # Create a button to submit the input
#         self.button = tk.Button(root, text="Submit", command=self.on_submit)
#         self.button.pack()

#     def on_submit(self):
#         # Get the input from the text entry box
#         input_text = self.entry.get()

#         # Set the label to display the input
#         self.label.config(text=input_text)

# # Create the root window
# root = tk.Tk()

# # Create an instance of the App class
# app = App(root)

# # Run the main loop
# root.mainloop()


import time
import requests
# from bs4 import BeautifulSoup


# def scrape(url):
#     # Make a GET request to the website
#     response = requests.get(url)

#     # Parse the HTML content
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Extract the information you want to scrape
#     # title = soup.find('h1').text
#     paragraphs = [p.text for p in soup.find_all('a')]
#     ps = [p.text for p in soup.find_all('p')]

#     # Print the information
#     # print(title)
#     print('\n'.join(paragraphs))
#     print('\n'.join(ps))


# # Test the scraper
# scrape('https://www.nytimes.com/section/world')
# Import webdriver from selenium library
from selenium import webdriver
# Importing keys in the program from webdriver
from selenium.webdriver.common.keys import Keys
# Providing the path of chrome Web driver
driver = webdriver.Chrome(
    '"C:/Users/callr/Downloads/chromedriver_win32/chromedriver.exe"')
# Opening url by get() method
i = 0
while i < 5000:
    # driver.get(
    #     "https://neokingyt.blogspot.com/2021/06/what-to-blog-about.html")
    # time.sleep(2)
    # driver.get(
    #     "https://neokingyt.blogspot.com/2022/12/recession-and-its-happening-in.html")
    # time.sleep(2)
    # driver.get(
    #     "https://neokingyt.blogspot.com/2022/12/inflation-and-its-effects-on-world.html")
    # time.sleep(2)
    # driver.get(
    #     "https://neokingyt.blogspot.com/2021/06/what-to-blog-about.html")
    # time.sleep(2)
    driver.get(
        "https://neokingyt.blogspot.com/2022/12/video-games-and-how-it-simulates-your.html")
    time.sleep(2)
    driver.get(
        "https://neokingyt.blogspot.com/2022/12/10-steps-to-be-best-version-of-yourself.html")
    time.sleep(12)
    i += 1
