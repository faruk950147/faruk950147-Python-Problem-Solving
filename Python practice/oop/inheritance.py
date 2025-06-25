class Vehicle:
    def __init__(self, name):
        self.name = name
        print("I'm from vehicle constructor")
    
    def VehicleName(self):
        print("I'm from vehicle method",self.name)
        
class Driver:
    def __init__(self, name):
        self.name = name
        print("I'm from driver constructor")
        
    def DriverName(self):
        print("I'm from driver method",self.name)
        

class Car(Vehicle, Driver):
    def __init__(self, name):
        super().__init__(name)
        print("I'm from car constructor")    
    def CarName(self):
        print("I'm from car method",self.name)
        

        
if __name__ =="__main__":
    v1 = Vehicle("Premio")
    v1.VehicleName()
    
    d1 = Driver("Faruk")
    d1.DriverName()
    
    c1 = Car("Audi")
    c1.CarName()
    c1.VehicleName()
    c1.DriverName()