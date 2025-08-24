#Parent Class
Class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

#Child class 1
class car ("Tundra")):
     def move(self):
       print ("Driving car")

#child class 2
class plane("Boeing 747"):
     def move(self):
       print("Flying Plane")

#Create instances of the child classes
my_car = Car()
my_plane = Plane()

#Call the 'move' method on each object
my_car.move()
my_plane.move()