
class smartdevice:
    def turn_on(self):
        print("Turning on device...")

class Smartphone(smartdevice):
    def turn_on(self):
        print("Smartphone: Booting mobile OS...")

class Smartwatch(smartdevice):
    def turn_on(self):
        print("Smartwatch: Starting wearable system...")


d = smartdevice()
s = Smartphone()
w = Smartwatch()

d.turn_on()
s.turn_on()
w.turn_on()
