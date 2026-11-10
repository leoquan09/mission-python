class Car:
    def __init__(self, model, make, speed):
        self.year_model = model
        self.make = make
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed
