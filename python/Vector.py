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
    def getMagnitude(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))

    def scalar(self, c):
        self.x *= c
        self.y *= c
        self.z *= c

    def add(self, v2):
        return Vector(self.x + v2.x, self.y + v2.y, self.z + v2.z, self.id + "+" + v2.id)

    def subtract(self, v2):
        return Vector(self.x - v2.x, self.y - v2.y, self.z - v2.z, self.id + "-" + v2.id)

    def dotProduct(self, v2):
        return (self.x * v2.x) + (self.y * v2.y) + (self.z * v2.z)

    def crossProduct(self, v2):
        return Vector((self.y * v2.z) - (self.z * v2.y), (self.x * v2.z) - (self.z * v2.x),
                      (self.x * v2.y) - (self.y * v2.x), self.id + "X" + v2.id)

    def isParralel(self, v2):
        test = Vector(0, 0, 0, self.id + "X" + v2.id)
        return self.crossProduct(v2) == test

    def isOrthoganal(self, v2):
        return self.dotProduct(v2) == 0

    def getAngle(self, v2):
        return math.acos((self.dotProduct(v2)) / (self.getMagnitude() * v2.getMagnitude()))

    def getAngleDegrees(self, v2):
        return self.getAngle(v2) * (180 / math.pi)

    def toString(self):
        return self.id + " = " + "<" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ">"


'''
V1 = Vector(1, 0, 0, "i")
V2 = Vector(0, 1, 0, "j")
V3 = Vector(0, 0, 1, "k")

print(Vector.toString(V1.add(V2)) + "\n" + Vector.toString(V1.subtract(V2)))
print(Vector.toString(V1.crossProduct(V2)))

V4 = V2.crossProduct(V3)
print(Vector.toString(V4))

if(V1.isParralel(V2)):
    print("yes")
'''


