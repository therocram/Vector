import math
from .Vector import Vector
from .Function import Function

class VectorField:
    def __init__(self, p, q, r, n):
        self.id = n
        self.P = Function(p)
        self.Q = Function(q)
        self.R = Function(r)

    def vectorAt(self, x, y, z):
        return Vector(self.P.valueAt(x, y, z),
                      self.Q.valueAt(x, y, z),
                      self.R.valueAt(x, y, z), self.id + "(" + str(x) + ", " + str(y) + ", " + str(z) + ")")

    def toString(self):
        return self.id + "(x, y, z)" + " = " + "<" + self.P.expression + ", " + self.Q.expression + ", " + self.R.expression + ">"


F = VectorField("ln(x)", "y-z", "z^2", "F")
print(F.toString())
print(F.vectorAt(1, 1, 1).toString())


