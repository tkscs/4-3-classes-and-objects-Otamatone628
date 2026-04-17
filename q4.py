import turtle as t
# Write a new class 'Point' with these methods:
# '__init__' sets 'self.x' and 'self.y'.
# '__str__' returns "(x,y)" for your object's x- and y-coordinates
# 'draw' :
#   1. uses 'turtle.goto' to go to that x and y coordinate
#   2. stamps a point with 'turtle.dot'
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def draw(self, t) :
        t.penup()
        t.goto(self.x, self.y)
        t.dot(10)

# Make 4 new objects of the class Point: (0, 0), (100, 0), (100, 100), (0, 100)
# Print your objects.
# Run your draw method for that object.
point_1 = Point(0,0)
point_2 = Point(100,0) 
point_3 = Point(100,100)
point_4 = Point(0,100)


points = [point_1, point_2, point_3, point_4]
for point in points:
    print(point)
    point.draw(t)

# OPTIONAL #
# The 'str' function will run the '__str__' method for an object. Use the 'turtle.write' method and the 'str' function to add a label to your point when you draw it.

t.exitonclick()
