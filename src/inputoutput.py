name = input("Enter your name: ")
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA: "))
is_student = input("Are you a student? (yes/no): ").lower() == 'yes'

print(f"Name: {name}, Age: {age}, GPA: {gpa}, Is Student: {is_student}")
print(f"Data types - Name: {type(name)}, Age: {type(age)}, GPA: {type(gpa)}, Is Student: {type(is_student)}")