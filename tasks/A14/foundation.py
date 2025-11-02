class vehicle:
    def start(self):
        print("vehicle starting....")
class car(vehicle):
    def start(self):
        print("car:vroom vroom!") 
class bike(vehicle):
    def start(self):
        print("bike:brum brum!") 
for vehicle in [car(),bike()]:
    vehicle.start()