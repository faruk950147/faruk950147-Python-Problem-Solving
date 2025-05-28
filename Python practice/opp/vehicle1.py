class Vehicle:
    def __init__(self, name, wheel, color, driver):
        self.name = name
        self.wheel = wheel
        self.color = color
        self.driver = driver
        
    def display(self): #This here self = car ok
        print("\n",self.name, "\n",self.wheel, "\n",self.color, "\n",self.driver)
        
if __name__ =="__main__":
    
    car = Vehicle("BMW", 4, "light black", "jamil")
    car.display()
    
    truck = Vehicle("TATA", 12, "yellow", "kamil")
    truck.display()