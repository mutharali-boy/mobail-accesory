
def student_list():
    print("Student List")
    students = ["Ali", "Fatima", "Bilal", "Sara"]
    print(students)
    index = int(input("Enter the index of the student (0,1,2,3): "))
    if index == 0:
        print("You selected:", students[0])
    elif index == 1:
        print("You selected:", students[1])
    elif index == 2:
        print("You selected:", students[2])
    elif index == 3:
        print("You selected:", students[3])
    else:
        print("Invalid index")

def student_details():
    print("Student Details")
    student_info = {'1': "Ali", '2': "101", '3': "A"}
    key = input("Enter key to see detail (Name, Roll No, Grade): ")
    if key == "1":
        print("Student Name:", student_info["1"])
    elif key == "2":
        print("Roll Number:", student_info["2"])
    elif key == "3":
        print("Grade:", student_info["3"])
    else:
        print("Invalid key")


def student_marks():
    print(" Enter Marks")
    marks = []  
    subjects = int(input("How many subjects do you want to enter marks for? "))
    for i in range(subjects):
        mark = int(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)
    print("Marks Entered:", marks)
    total = sum(marks)
    print(" Total Marks:", total)


def calculator():
    print("Calculator")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")
    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        print("Result:", a / b)
    else:
        print("Invalid operator")

print("MENU")
print("1.Show Student List")
print("2.Student Details")
print("3.Enter Marks")
print("4.Calculator")


choice = int(input("\nEnter your choice (1–4): "))

if choice == 1:
    student_list()
elif choice == 2:
    student_details()
elif choice == 3:
    student_marks()
elif choice == 4:
    calculator()
else:
    print(" Invalid choice.")
