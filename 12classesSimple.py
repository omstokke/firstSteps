#Classes are used to define new types to model complex concepts
#Naming classes with Capital on every word (Pascal) and not camelCase
class Point:
    def __init__(self, x, y): #a constructor, short for initialize, gets called when the object is created/called in the program - "contructs an object"
        self.x = x #creates an attribute x and adds it to the current object
        self.y = y
    
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")


#Objects are an instance of a class
point1 = Point(0, 0) #creating a specific object: point1
point1.draw() #calling method draw
point1.move() #calling method move
point1.x = 10 #giving the object point1 an attribute x (which = 10)
point1.y = 20 #giving the object point2 a new attribute y (which = 20)

print(point1.x)
print(point1.y)

point2 = Point(1, 2) #a new object, point2 - sets an x- and y-value using the constructor
#the 'self' refers back to the object used - here point2 - which again creates the attribute
print(point2.x) #can be called without defining the attribute in the code, as it is defined when calling the object using the Point-class and two arguments (1 and 2)
print(point2.y)