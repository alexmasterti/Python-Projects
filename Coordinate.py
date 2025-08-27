class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"

x = Coordinate(2,3)
print(x)
print(type(x))
print(x.x)
origin = Coordinate(0,0)
print(origin.x)
print(x.distance(origin))
