# Single responsibility
#Každá třída má svou funkci. Jedna třída má svou zodpovědnost

# Single responsibility

class User:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0 or age >= 130:
            raise ValueError("Age must be between 0 and 130 ")
        self._age = age

class Console:
    @staticmethod
    def display(obj):
        print(f"{obj.name} {obj.last_name} {obj.age}")

    @staticmethod
    def input(obj):
        obj.name = input("Input name:")
        obj.last_name = input("Input last name:")
        obj.age = int(input("Input age:"))

obj = User("Bill", "Windows", 34)
Console.display(obj)
obj = Console.input()
Console.display(obj)



