class Vehicle:
    coll = "TMSS TECHNICAL INSTITUTE (TTI)"#this is class veriable
    def __init__(self, name, wheel, color, driver):
        self.name = name
        self.wheel = wheel
        self.color = color
        self.driver = driver
        
    def display(self): #This here self = car ok
        print("\n",self.name, self.coll,"\n",self.wheel, self.coll,"\n",self.color, self.coll,"\n",self.driver, self.coll)
        
if __name__ =="__main__":
    car = Vehicle("Premio", 4, "light black", "jamal")
    car.display()
    
    truck = Vehicle("TATA", 12, "yellow", "kamil")
    truck.display()



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