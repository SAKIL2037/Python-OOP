class student:
    ID = ""
    CGPA = ""

    def __init__(self,ID,CGPA):
        self.ID = ID
        self.CGPA = CGPA

    def Display(self):
        print(f"ID :{self.ID},CGPA : {self.CGPA}")


sakil = student(105,3.75)
print(isinstance(sakil,student))
sakil.Display()