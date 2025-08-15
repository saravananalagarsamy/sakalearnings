flag = True
while flag:
    user_input = input("Enter 'exit' to stop the loop: ")
    if user_input.lower() == 'exit':
        flag = False
    else:
        print(f"You entered: {user_input}")
print("Loop has ended.")    