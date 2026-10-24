name = input("Enter student name: ")
reg_no = input("Enter register number: ")
department = input("Enter department: ")
marks = int(input("Enter marks: "))

if 0 <= marks <= 100:
    print("Student Details")
    print("Name:", name)
    print("Register Number:", reg_no)
    print("Department:", department)
    print("Marks:", marks)
    print("Student details feature completed")
else:
    print("Invalid marks")
    
