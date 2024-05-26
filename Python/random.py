class B:
    def __get__(self,obj,objtype = None):
        return obj.x * obj.y

class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    area = B()
a = A(5,7)
print(a.area)
a.y = 10
print(a.area)