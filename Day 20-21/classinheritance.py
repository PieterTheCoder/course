class Animal:
    def __init__(self,):
        self.name = "Animal"

    def bark(self):
        print("Woof, woof")

class Dog(Animal):
    def __init__(self):
        super().bark()
        print("Greetings sir.")

Golden_Retriever = Dog()
print(Golden_Retriever.bark)
