class Area:
    def __init__(self):
        self.al = 0
        self.ba = 0

    def nums(self):
        self.al = int(input("Ingresa la base del triangulo: "))
        self.ba = int(input("Ingresa la altura del triangulo: "))

    def area(self):
        return (self.ba * self.al)/2

    def result(self):
        result = self.area()
        print("El area del triangulo es:", result)
        
        
def area_terminada():
    operacion = Area()
    operacion.nums()
    operacion.result()

area_terminada()    
