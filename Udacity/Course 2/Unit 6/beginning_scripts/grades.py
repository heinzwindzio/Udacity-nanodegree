names =  input("Enter names separated by commas: ") # get and process input for a list of names
assignments = input("Enter number of assignments separated by commas: ") # get and process input for a list of the number of assignments
grades =  input("Enter grades separated by commas: ") # get and process input for a list of grades

names_list = names.split(",")
assignments_list = assignments.split(",")
grades_list = grades.split(",")

## message string to be used for each student
## HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. Your current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

## write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for x in range(len(names_list)):
    print(message.format(names_list[x], assignments_list[x], grades_list[x], str(int(grades_list[x]) + 2 * int(assignments_list[x]))))