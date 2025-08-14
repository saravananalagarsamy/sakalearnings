name = "john"
age = 30
gpa = 3.5
is_student = True

print(f"Name: {name}, Age: {age}, Is Student: {is_student}")
print(f"Data types - Name: {type(name)}, Age: {type(age)}, Is Student: {type(is_student)}")

def typecast_example():
    num_str = "100"
    num_int = int(num_str)
    print(f"String to Integer: {num_str} -> {num_int}, Type: {type(num_int)}")

typecast_example()