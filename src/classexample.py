class Human:
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city

    def display_info(self) -> None:
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")

male: Human = Human("sara", 30, "New York")
male.display_info()

female : Human = Human("lka", 25, "Los Angeles")
female.display_info()