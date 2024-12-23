class Vehicle:

    def __init__(self,make,model):
        self.make = make
        self.model = model

    def get_info(self):
        return f'Марка: {self.make}\nМодель: {self.model}'

VAZ2108 = Vehicle('VAZ',2108)
print(VAZ2108.get_info())

class Car(Vehicle):

    def __init__(self, make, model, fuel_type):
        super().__init__(make,model)
        self.fuel_type = fuel_type

    def get_info(self):
        return f'Марка: {self.make}\nМодель: {self.model}\nТип топлива: {self.fuel_type}'

VAZ2110 = Car('VAZ',2110, 'Бензин')

print(VAZ2110.get_info())
