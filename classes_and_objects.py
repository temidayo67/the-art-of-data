class vehicleType:
    def __init__ (self, name, kind, color, value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value

    def carDescription(self):
        descr_str = f"{self.name} is a {self.color} {self.kind} and it's worth {self.value}"
        return descr_str

car1 = vehicleType('Fer','convertible', 'red', '$60,000')
car2 = vehicleType('Jump', 'van', 'blue', '$10,000')

print(car1.carDescription())
print(car2.carDescription())
