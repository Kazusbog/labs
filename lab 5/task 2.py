class Circle:
    def __init__(self: object, radius:int):
        self.radius = radius
    def get_radius(self:object):
        return self.radius
    def set_radius(self:object, radius:int):
        self.radius = radius
circle = Circle(10)
circle1 = Circle(20)

print(circle.get_radius())
print(circle1.get_radius())

circle.set_radius(12)
circle1.set_radius(15)

print(circle.get_radius())
print(circle1.get_radius())