class Vector2:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

pos01 = Vector2(5,8)
pos02 = Vector2(2,4)
pos03 = pos01 - pos02
print(pos03.__dict__)


class VectorNew2:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

pos01 = VectorNew2(5,8)
print(id(pos01))
pos02 = VectorNew2(2,4)
pos01 -= pos02
print(pos01.__dict__)
print(id(pos01))