import os

cwd = os.getcwd()
file_path = cwd + "\\Udacity\\Course 2\\Python Scripting for AI programming\\read\\file.txt"

names = []
name_title = []

try:
    with open(file_path, 'r') as file:
        for line in file:
            name_title = line.split(',')
            names.append(name_title[0])
        print(names)
except FileNotFoundError as fnf:
    print('Could not find the file!', fnf)
finally:
    print('Closing the try statement')











