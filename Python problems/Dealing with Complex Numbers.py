import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real                # a or c
        self.imaginary = imaginary      # b or d
        return

    def __add__(self, no):
        real = self.real + no.real            # a + c
        imaginary = self.imaginary + no.imaginary  # b + d
        return Complex(real, imaginary)

    def __sub__(self, no):
        real = self.real - no.real            # a - c
        imaginary = self.imaginary - no.imaginary  # b - d
        return Complex(real, imaginary)

    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary  # ac - bd
        imaginary = self.real * no.imaginary + self.imaginary * no.real  # ad + bc
        return Complex(real, imaginary)

    def __truediv__(self, no):
        real = (self.real * no.real + self.imaginary * no.imaginary) / \
            (no.real ** 2 + no.imaginary ** 2)  # (ac + bd)/(c^2 + d^2)
        imaginary = (self.imaginary * no.real - self.real * no.imaginary) / \
            (no.real ** 2 + no.imaginary ** 2)  # (bc - ad)/(c^2 + d^2)
        return Complex(real, imaginary)

    def mod(self):
        mod = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(mod, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
