from datetime import datetime

def print_current_datetime() -> None:
    console_output = f"Current date and time: {datetime.now()}"
    print(console_output)

print_current_datetime()    