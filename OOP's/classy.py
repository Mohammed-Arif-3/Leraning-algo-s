class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("the constructor worked")
s1=Student("arif",93)
print(s1.name,s1.marks)