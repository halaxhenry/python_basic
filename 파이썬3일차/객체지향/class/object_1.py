class Car:
    color = ""
    speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value


car = Car()
print(car.speed)
car.upSpeed(50)
print(car.speed)
