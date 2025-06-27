# def add(a: int, b: int) -> int:
#     return a + b

# if __name__ == "__main__":
#     print(add(1, 2))

# class Adder:
#     def __init__(self, a: int, b: int):
#         self.a = a
#         self.b = b

#     def add(self) -> int:
#         return self.a + self.b

# if __name__ == "__main__":
#     adder = Adder(1, 2)
#     print(adder.add())
    

class User:
    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self) -> str:
        return f"User(name={self.name}, age={self.age}, email={self.email})"

if __name__ == "__main__":
    user = User("John", 30, "john@example.com")
    print(user)