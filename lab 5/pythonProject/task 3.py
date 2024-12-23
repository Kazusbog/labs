from functools import reduce


class Vehicle:

    reduce = 10

    def __init__(self,door,color_in,color_out,numbers,fuel):
        self.door = door
        self.color_in = color_in
        self.color_out = color_out
        self.numbers = numbers
        self.fuel = fuel

    def get_color(self):
        return 'in ' +  f"{self.color_in}" + '\t out ' + f"{self.color_out}"

    def get_numbers(self):
        return f"{self.numbers}"

    def set_color(self,color_out):
        self.color_out=color_out
    def set_numbers(self,numbers):
        self.numbers=numbers

    def ride(self, km):
        a = km / 100
        self.fuel = self.fuel - (a / Vehicle.reduce * 1000)



color_in = 'red'
color_out = 'red'
numbers = 'A777AA777'
fuel = 3000

VAZ2108 = Vehicle('close',color_in,color_out, numbers,fuel)
print(VAZ2108.get_color())
print(VAZ2108.get_numbers())
VAZ2108.set_color('gray')
VAZ2108.set_numbers('A321BC31')
print(VAZ2108.get_color())
print(VAZ2108.get_numbers())
VAZ2108.ride(50)
print(VAZ2108.fuel)

