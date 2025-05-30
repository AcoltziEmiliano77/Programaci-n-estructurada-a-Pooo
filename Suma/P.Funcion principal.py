class Suma:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def nums(self):
        self.num1 = int(input("Ingresa el numero 1: "))
        self.num2 = int(input("Ingresa el numero 2: "))

    def suma(self):
        return self.num1 + self.num2

    def result(self):
        result = self.suma()
        print("El resultado de la suma es:", result)
        
        
def suma_terminada():
    operacion = Suma()
    operacion.nums()
    operacion.result()

suma_terminada()    
