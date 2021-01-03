class triangle:

    def __init__(self,base,height):
        self.base = base
        self.height = height

    def calculate_area(self):
        area = (self.base * self.height)/2
        print(f"Triangle area : {area}")



t1 = triangle(10,20)
t1.calculate_area()
t2 = triangle(20,30)
t2.calculate_area()