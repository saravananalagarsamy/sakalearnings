def operations():
    full_name = "Saka"
    age = 25
    score = 95.5
    
    if(score > 35):
        status = True
    else:
        status = False
    if (status):
        print(f"{full_name} is {age} years old and has passed with a score of {score}.")
    else: 
        print(f"{full_name} is {age} years old and has failed with a score of {score}.")    

    print (f"average score is {score//2}.")
    age = age + 1
    score = 35

def pass_fail():
    print("This function checks pass or fail status based on score.")


operations()    