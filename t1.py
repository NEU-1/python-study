class Circle():
    pi = 3.14
    def __init__(self, r):
        self.r = r
    def __str__(self):
        return f' {self.r}'
c1 = Circle(5)
c2 = Circle(10)

print(Circle.pi)
print(c1.pi)
print(c1)