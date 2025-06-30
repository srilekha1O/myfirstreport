class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        print(f"Name: {self.name}, roll:{self.roll}")
s1=student("Srilekha",27)
s1.display()