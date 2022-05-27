class Circle():
    def __init__(self,r):
        self.r=r
    def diametr_circle_is(self):
            print(self.r+self.r)
            print("Діаметр знайдено")

    def s_circle_is(self):
         print(self.r*self.r*3,14)
         print("Площа знайдена")

c1=Circle(793)
c2=Circle(526)

c1.diametr_circle_is()
c1.s_circle_is()
c2.diametr_circle_is()
c2.s_circle_is()