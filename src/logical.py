# or and not 
# Logical operations in Python
def logical_operations(a, b):
    # and operation
    if a and b:
        print(f"a and b: {a and b}")
    elif a or b:
        # or operation
        print(f"a or b: {a or b}")
    # not operation
    elif (not a and not b):
        print(f"not a: {not a}, not b: {not b}")
    else:
        print("Both values are False")

logical_operations(True, False)
logical_operations(True, True)
logical_operations(False, False)
