class rec():
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return float(self.length * self.breadth)
        



r = rec(20,30.81)


print("Area of Rectangle: ",r.area())


