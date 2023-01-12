import os

file = os.open('details1.txt', os.O_RDONLY)
cont = os.read(file, 1)
print(cont)
os.close(file)
# os.rename('details.txt', 'details1.txt')
# os.system('cmd')
print(os.getcwd())
os.chdir('C:\\Users\\callr\\Python100\\myenv')
print(os.getcwd())
print(os.listdir())
