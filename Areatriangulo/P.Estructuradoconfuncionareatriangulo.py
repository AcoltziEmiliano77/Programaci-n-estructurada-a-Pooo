def cal():
	print("Ingresa la base del triangulo")
	ba = float(input())
	print("Ingresa la altura del triangulo")
	al = float(input())
	area = (ba*al)/2
	print("El area del triangulo es: ",area)
	return area

if __name__ == '__main__':
	area = cal()

