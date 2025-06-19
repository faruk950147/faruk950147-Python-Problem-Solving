def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))

class Adder:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def add(self) -> int:
        return self.a + self.b

adder = Adder(1, 2)
print(adder.add())