class Area:
    def __init__(self):
        self.ba = 0
        self.al = 0

    def nums(self):
        while True:
            try:
                self.ba = int(input("Ingresa la base del triangulo: "))
                break
            except ValueError:
                print("Error chavalin")
        
        while True:
            try:
                self.al = int(input("Ingresa la altura del triangulo: "))
                break
            except ValueError:
                print("Error chavalin")

    def area(self):
        return (self.ba * self.al)/2

    def result(self):
        result = self.area()
        print("El area del triangulo es:", result)

operacion = Area()
operacion.nums()
operacion.result()
