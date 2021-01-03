class student:
    ID = ""
    CGPA = ""

    def set_value(self,ID,CGPA):
        self.ID = ID
        self.CGPA = CGPA

    def Display(self):
        print(f"ID :{self.ID},CGPA : {self.CGPA}")


sakil = student()
print(isinstance(sakil,student))
sakil.set_value(101,3.80)
sakil.Display()