class Area:
    def __init__(self):
        self.ba = 0
        self.al = 0

    def nums(self):
        self.ba = int(input("Ingresa la base del triangulo: "))
        self.al = int(input("Ingresa la altura del triangulo: "))

    def area(self):
        return (self.ba * self.al)/2

    def result(self):
        result = self.area()
        print("El resultado es:", result)

operacion = Area()
operacion.nums()
operacion.result()
