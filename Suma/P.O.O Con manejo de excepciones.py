class Suma:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def nums(self):
        while True:
            try:
                self.num1 = int(input("Ingresa el numero 1: "))
                break
            except ValueError:
                print("Error chavalin")
        
        while True:
            try:
                self.num2 = int(input("Ingresa el numero 2: "))
                break
            except ValueError:
                print("Error chavalin")

    def suma(self):
        return self.num1 + self.num2

    def result(self):
        result = self.suma()
        print("El resultado de la suma es:", result)

operacion = Suma()
operacion.nums()
operacion.result()
