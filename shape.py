from cmath import pi


class Circle:
    def __init__(self,r):
        self.r=r


    def area(self):
        pi=3.14
        total_radius=self.r*self.r
        area=pi*total_radius
        return area
    def circumference(self):
       circumference=2*pi*self.r
       return circumference
class Square:
    def __init__(self,a):
      self.a=a
    def Area(self):
        A=self.a*self.a
        return A

    def perimeter(self):
        p=self.a*4
        return p

class Rectangle:
    def __init__(self,w,l):
        self.w=w
        self.l=l
    def area(self):
        A=self.w*self.l
        return A

    def Perimeter(self):
        p=2(self.w*self.l)
        return p

class Sphere:
    def __init__(self,r):
      self.r=r
      
    def surfaceArea(self):
        A=4*pi*self.r*self.r
        return  A
    
    def volume(self):
        V=4/3*pi*self.r*self.r*self.r
        return V
    