from Car import Car

car = Car("Toyota Subaru", "Civic", 0)

for i in range(5):
    print(car.get_speed())
    car.accelerate()

for i in range(5):
    print(car.get_speed())
    car.brake()
