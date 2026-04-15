class Animal:
    def __init__(self,):
        self.name = "Animal"

    def bark(self):
        print("Woof, woof")

    def give_food(self):
        print("Hwere is my fwood")

class Dog(Animal):
    def __init__(self):
        super().bark()
        print("Greetings sir.")

Golden_Retriever = Dog()
print(Golden_Retriever.give_food)
