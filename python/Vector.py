import math
from typing import List, Any


class Vector:

    def __init__(self, a, b, c, n):
        self.x: float = a
        self.y: float = b
        self.z: float = c
        self.id: str = n

    #
    #	def __init__(self):
    #		self(0, 0, 0, "a")
    #
    #	def __init__(self, v):
    #
    #		self(v.x, v.y, v.z, v.id)
    #
    #

    def setx(self, a):
        self.x = a

    def sety(self, b):
        self.y = b

    def setz(self, c):
        self.z = c

    def name(self, n):
        self.id = n

    def magnitude(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))

    def scalar(self, c):
        self.x *= c
        self.y *= c
        self.z *= c

    def add(self, v):
        return Vector(self.x + v.x, self.y + v.y, self.z + v.z, self.id + " + " + v.id)

    def subtract(self, v):
        return Vector(self.x - v.x, self.y - v.y, self.z - v.z, self.id + " - " + v.id)

    def dot(self, v):
        return (self.x * v.x) + (self.y * v.y) + (self.z * v.z)

    def cross(self, v):
        return Vector((self.y * v.z) - (self.z * v.y), (self.x * v.z) - (self.z * v.x),
                      (self.x * v.y) - (self.y * v.x), self.id + " X " + v.id)

    def isParralel(self, v):
        return (self.cross(v)).x == 0 and (self.cross(v)).y == 0 and (self.cross(v)).z == 0

    def isOrthoganal(self, v):
        return self.dot(v) == 0

    def getAngle(self, v):
        return math.acos((self.dot(v)) / (self.magnitude() * v.magnitude()))

    def getAngleDegrees(self, v):
        return self.getAngle(v) * (180 / math.pi)

    def toString(self):
        return self.id + " = " + "<" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ">"



V1 = Vector(1, 0, 0, "i")
V2 = Vector(0, 1, 0, "j")
V3 = Vector(0, 0, 1, "k")

print(Vector.toString(V1.add(V2)) + "\n" + Vector.toString(V1.subtract(V2)))
print(Vector.toString(V1.cross(V2)))

V4 = V2.cross(V3)
V4.name("V")
print(Vector.toString(V4))

if(V1.isParralel(V2)):
    print("yes")



