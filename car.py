class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def display(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:{}\n".format(self.tax)

ford = Car(1000, "35mph", "full", "15mph")
toyota = Car(2000, "5mph", "Not full", "15mph")
subaru = Car(2000, "15mph", "Kind of full", "95mph")
corvette = Car(2000, "25mph", "Full", "25mph")
mazda = Car(2000, "45mph", "Empty", "25mph")
lexus = Car(20000000, "25mph", "Empty", "15mph")

ford.display()
toyota.display()
subaru.display()
corvette.display()
mazda.display()
lexus.display()