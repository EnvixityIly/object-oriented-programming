class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
tesla = Vehicle(180,0)
lambo = Vehicle(350,3)

print("Tesla max speed", tesla.max_speed)
print("Tesla mileage",tesla.mileage)

print("Lambo max sped:" , lambo.max_speed)
print("Lambo mileage", lambo.mileage)