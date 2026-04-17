class Dog:
    """a dog"""
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"A dog named {self.name}🐾"
    def speak(self):
        print(f"{self.name} says woof!🐾")

lizzie = Dog("Lizzie")
lizzie.speak()
print(lizzie)