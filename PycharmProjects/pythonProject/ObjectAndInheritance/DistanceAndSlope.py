class Line(object):

    def __init__(self, coor1, coor2):
        self.coordinate_1 = coor1
        self.coordinate_2 = coor2

    def distance(self):
        x1, y1 = self.coordinate_1
        x2, y2 = self.coordinate_2
        Distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
        return Distance

    def slope(self):
        x1, y1 = self.coordinate_1
        x2, y2 = self.coordinate_2
        Slope = (y2 - y1) / (x2 - x1)
        return Slope


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())
