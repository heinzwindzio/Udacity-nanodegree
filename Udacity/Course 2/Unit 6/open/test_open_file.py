file = open("new_file.txt", 'w')

file.write("Hello World")

file.close()

#use with to auto close a file
with open("new_file2.txt", 'w') as f:
    f.write("Yo")

f2 = open("new_file2.txt", 'r')
file_data = f2.read()
print(file_data)
