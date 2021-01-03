class student:
    ID = ""
    CGPA = ""


sakil = student()
print(isinstance(sakil,student))
sakil.ID = 101
sakil.CGPA = 3.86
print(f"ID : {sakil.ID},CGPA : {sakil.CGPA}")


Ratul = student()
print(isinstance(Ratul,student))
Ratul.ID = 102
Ratul.CGPA = 3.50
print(f"ID : {Ratul.ID},CGPA : {Ratul.CGPA}")
