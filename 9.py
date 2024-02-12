# 6. Object-Oriented Programming

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

# Instantiate objects
dog1 = Dog("Gucci", 3)
dog2 = Dog("Popsy", 5)

# Call methods
print(f"{dog1.name} says: {dog1.bark()}")
print(f"{dog2.name} says: {dog2.bark()}")
