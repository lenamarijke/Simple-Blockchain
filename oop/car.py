import vehicle

# inherit from Vehicle class
class Car(vehicle.Vehicle):

    def brag(self):
        print('Look how cool my car is')

    
car1 = Car()
car1.drive()
car1.add_warning('New Warning')
# print object as a dictironary
# print(car1.__dict__)

print(car1)

car2 = Car(200)
car2.drive()