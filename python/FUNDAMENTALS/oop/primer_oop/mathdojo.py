class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for x in nums:
            self.result += x
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for x in nums:
            self.result -= x
        return self


# crear una instancia:
md = MathDojo()

# probar los métodos
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)  # debería imprimir 5

# ejecutar los métodos unas cuantas veces más y verificar el resultado
x = md.add(10).add(5, 1).subtract(3, 2).result
print(x)  # debería imprimir 16

y = md.add(100, 200, 300).subtract(50, 25).result
print(y)  # debería imprimir 541
