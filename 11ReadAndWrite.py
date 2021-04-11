employee_file = open("Employees.txt", "r") #Opens the relative path to Employees in read-mode - see also write and append w/a, and r+ (read and write)

#print(employee_file.readable()) #Checks if your file is readable
#print(employee_file.read()) #Prints everything in the file, and moves the cursor to after the last line of content
#print(employee_file.readline())#Prints a single line from the file and moves the cursor to the next line
#print(employee_file.readlines()) #Produces and prints an array list of the lines in the file

list_of_employees = []

for employee in employee_file.readlines():
    list_of_employees.append(employee.strip("\n"))

print(list_of_employees)

employee_file.close() #Always close your files

#employee_file = open("Employees.txt", "a") # Append-mode

#employee_file.write("\nToby - Human Resources") # Appends to the last line of content, so needs newline chars

#employee_file.close()

#Can also use '(w)rite'-mode to create new files,
# Extensions are variable, for example: HTML, .txt., .csv, and so on
# the write-function with "w"-mode replaces the content with what is being written
# Uses: To write/append to any file using input/reads/whatever