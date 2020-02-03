from vehicle import Vehicle

class Bus(Vehicle):
    
# special method for constructs
    def __init__(self, starting_top_speed=100):
        # call constructor of base class with super()
        super().__init__(starting_top_speed)
        self.passengers = []
    
    
    def add_group(self, passengers):
        self.passengers.extend(passengers)


bus1 = Bus(150)
bus1.add_group(['Lena', 'Jens'])
print(bus1.passengers)
