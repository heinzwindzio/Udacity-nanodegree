f1= open("new_file.txt", 'w')
f1.write("Hello World")
f1.close()

#use with to auto close a file
with open("new_file2.txt", 'w') as f2:
    f2.write("Yoooooo\n")
    f2.write("Second Line")


with open("new_file2.txt", 'r') as f2:
    for line in f2:
        print(line.strip())




