import random


class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


cars = []

for i in range(10):
    registration_number = "ABC-" + str(i + 1)
    maximum_speed = random.randint(150, 200)

    car = Car(registration_number, maximum_speed)
    cars.append(car)


while True:

    for car in cars:
        change = random.randint(-10, 15)

        car.accelerate(change)
        car.drive(1)

    for car in cars:
        if car.travelled_distance >= 10000:
            break
    else:
        continue

    break


print("Car Race Results")
print("------------------------------")

for car in cars:
    print(
        car.registration_number,
        car.maximum_speed,
        car.current_speed,
        car.travelled_distance
    )
