name = input("Enter your name: ")
score = int(input("Enter your score: "))
if(score > 50):
    print(f"{name} has passed with a score of {score}.")
else:
    print(f"{name} has failed with a score of {score}.")
print(f"Data type of score: {type(score)}")