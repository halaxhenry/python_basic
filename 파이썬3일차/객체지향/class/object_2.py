class Car:
    color = ""
    speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value


myCar1 = Car()
myCar1.color = "빨강"
myCar1.speed = 0

myCar2 = Car()
myCar2.color = "파랑"
myCar2.speed = 0

myCar3 = Car()
myCar3.color = "노랑"
myCar3.speed = 0

myCar1.upSpeed(3000)
print(f"myCar1의 색상은 {myCar1.color}, myCar1의 속도는 {myCar1.speed}")

myCar2.upSpeed(20)
print(f"myCar2의 색상은 {myCar2.color}, myCar2의 속도는 {myCar2.speed}")

myCar3.upSpeed(50)
print(f"myCar3의 색상은 {myCar3.color}, myCar3의 속도는 {myCar3.speed}")
