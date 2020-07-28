import math


class Function:
    expression: str

    def __init__(self, n):
        self.expression = n

    def valueAt(self, x, y, z):
        f: float = 0  # final return value
        eq = self.expression.strip()  # trim expression
        while eq != "":
            # if eq.find("+") == -1: #eq.find("+") == eq.find("-"):
            # w = eq

            if eq.find("(") != -1 and eq.rfind(")") != -1:
                n = self.expression
                self.expression = eq[(eq.find("(") + 1): eq.rfind(")")]
                # print(self.expression)
                # print(str(self.valueAt(x, y, z)))
                eq = eq.replace(eq[eq.find("("): (eq.rfind(")") + 1)], str(self.valueAt(x, y, z)))
                # print(eq)
                self.expression = eq
                f += self.valueAt(x, y, z)
                self.expression = n
                break
            else:
                while (eq.rfind("+") != -1 and eq.rfind("+") != 0) or (eq.rfind("-") != -1 and eq.rfind("-") != 0):
                    if eq.find("+") != -1:
                        w = eq[:eq.find("+")]
                        q = eq[(eq.find("+") + 1):]
                        n = self.expression
                        self.expression = w
                        f += self.valueAt(x, y, z)
                        self.expression = q
                        f += self.valueAt(x, y, z)
                        self.expression = n
                        # print(str(f))
                        eq = eq.replace(eq, "0")
                    if eq.find("-") != -1:
                        w = eq[:eq.find("-")]
                        q = eq[(eq.find("-") + 1):]
                        n = self.expression
                        self.expression = w
                        # print(self.valueAt(x, y, z))
                        f += self.valueAt(x, y, z)
                        self.expression = q
                        # print(self.valueAt(x, y, z))
                        f -= self.valueAt(x, y, z)
                        self.expression = n
                        eq = eq.replace(eq, "0")

                else:
                    f += self.evaluate(self.varReplace(eq, x, y, z))
                    break

        return f

    def evaluate(self, word):
        word.strip()
        if word.find("ln") != -1:
            try:
                return math.log(float(word[(word.find("n") + 1):]))  # takes natural log of a
            except ValueError:
                print("Domain error:\n\t for any ln(a), a > 0")
                exit()
        elif word.find("^") != -1:  # if a^x, where x is some number, then
            return math.pow(float(word[:word.find("^")]),
                            float(word[(word.find("^") + 1):]))  # compute a to the power of everything after "^"
        elif word.find("sin") != -1:
            return math.sin(float(word[(word.find("n") + 1):]))
        elif word.find("cos") != -1:
            return math.cos(float(word[(word.find("s") + 1):]))
        elif word.find("tan") != -1:
            return math.sin(float(word[(word.find("n") + 1):]))
        else:
            # if word.find("+") == 0:
            #   word = word.replace("+", "", 1)
            return float(word)

    def varReplace(self, word, a, b, c):
        while word.find("x") != -1:
            word = word.replace("x", str(a))
        while word.find("y") != -1:
            word = word.replace("y", str(b))
        while word.find("z") != -1:
            word = word.replace("z", str(c))

        return word


'''
fun = input("Enter expression: ")
F = Function(fun)
# print(str(float("5-2")))
print(str(F.valueAt(5, 1, -2)))
# print(str(+5))
'''
'''  
    def varSearch(self, word, x, y, z):
        a = word.find("x")
        b = word.find("y")
        c = word.find("z")

        if b == -1 and c == -1:
            self.single(word, x)
        elif a == -1 and c == -1:
            self.single(word, y)
        elif a == -1 and b == -1:
            self.single(word, z)
        else:
            #multi(word, x, y, z)

    def single(self, word, a):
        word.strip()
        n = ""
        g = 0
        if word == "lna":
            return math.log(a) #takes natural log of a
        elif word == "a":
            return a
        elif word.find("a^") != -1:                                 #if a^x, where x is some number, then
            return math.pow(a, float(word[(word.find("^") + 1):]))  #compute a to the power of everything after "^"
        elif word.find("^a") != -1:                                 #if x^a, where x is some number, then
            return math.pow(float(word[:(word.find("^"))]), a)      #compute everything before "^" to the power of a
        elif word.find("sin") != -1:
            if word.find("(") != -1 and word.find(")") != -1:
                n = self.expression
                self.expression = word[(word.find("(") + 1): word.find(")")]
                g += self.valueAt(a, a, a)
'''
