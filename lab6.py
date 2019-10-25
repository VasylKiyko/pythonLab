"""
у цій лабораторній я продемонструю на прикладі декількох класів dependency injection
"""


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name


class Car:
    def __init__(self, name, driver):
        self.name = name
        self.driver = driver

    def ride(self):
        print("{} drive a car {}".format(self.driver.getName(), self.name))

    def changeDriver(self, driver):
        if driver.age >= 18:
            self.driver = driver
        else:
            print('This person is too young!!')


if __name__ == '__main__':
    person1 = Driver('Vasyl', 19)
    person2 = Driver('Sofia', 16)
    print(person1.getName())
    car = Car('Opel', person1)
    car.ride()
    car.changeDriver(person2)
    car.ride()
