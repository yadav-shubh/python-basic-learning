class Calculator:
    def sum(self, a):
        print(f"sum of 1 arg sum: {a}")

    def sum(self, a, b):
        print(f"sum of 2 arg sum: {a + b}")

    def sum(self, a, b, c):
        print(f"sum of 3 arg sum: {a + b + c}")


calc = Calculator()
print(calc.sum(1))
