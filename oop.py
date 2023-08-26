class Vehicle:
    name = ""
    wheels = 0
    speed = 0
    color = ""

    def __init__(self , name):
        self.name = name
        print("init vehicle class")

    def move(self):
        print("move in Vehicale class ")

class Car(Vehicle):
    doors = 0
    fuel = 0
    start = ""
    engine = 0
    name = ""
    
    def __init__(self):
        print("init car class ")
        super().__init__("benz")
   
    def move(self):
        print("move in Car class ")

benz500 = Car()
print(benz500.name)
benz500.move()
benz500.name = "benz500"
benz500.color = "black" 
benz500.doors = 4
 
print("benz500 :" , benz500.name)


#   Person.__init__(self, fname, lname)





