class Car:
    static_var = 10

    def __str__(self):
        return str(self.static_var)


car1 = Car()
car2 = Car()
print(car1)
print(car2)

car1.static_var = 20
print(car1)
print(car2)
