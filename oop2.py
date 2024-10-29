class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def display(self):
        print(f"My name is {self.name},I am a {self.gender} aged {self.age} years.")

myname=person("Lilian", 22,"Female")
myname.display()