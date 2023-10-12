class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        Volume = Cylinder.pi * self.height * (self.radius) ** 2
        return Volume

    def surface_area(self):
        SurfaceArea = (2 * Cylinder.pi * (self.radius) ** 2) + (2 * Cylinder.pi * self.radius * self.height)
        return SurfaceArea


c = Cylinder(20)
print(c.radius)
print(c.height)
