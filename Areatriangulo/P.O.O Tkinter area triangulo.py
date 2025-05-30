import tkinter as tk
from tkinter import Entry, ttk, messagebox

def Area():
	try:
		ba = int(entry1.get())
		al = int(entry2.get())
		area = (ba * al)/2
		messagebox.showinfo("Resultado", f"El area del triangulo es: {area}")
	except ValueError:
		messagebox.showerror("Error chavalin", "Por favor ingresa numeros validos crack")		
		
root = tk.Tk()
root.title("Area del triangulo chaval")
root.geometry("700x400")

label1 = tk.Label(root, text="Ingresa la base del triangulo:")	
label1.pack(pady=10)
entry1 = Entry(root)
entry1.pack(pady=10)	
label2 = tk.Label(root, text="Ingrese la altura del triangulo:")
label2.pack(pady=10)
entry2 = Entry(root)
entry2.pack(pady=10)
button = ttk.Button(root, text="Sacar area", command=Area)
button.pack(pady=20)
root.mainloop()