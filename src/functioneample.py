from datetime import datetime

def print_current_datetime() -> str:
    console_output = f"Current date and time: {datetime.now()}"    
    return console_output

def hello_world(name: str) -> None:
    print(f"Hello, {name}! Today is {print_current_datetime()}")

hello_world(input("Enter your name :"))    