import tkinter as tk
from tkinter import Entry, ttk, messagebox

def suma():
	try:
		n1 = int(entry1.get())
		n2 = int(entry2.get())
		suma = n1 + n2
		messagebox.showinfo("Resultado", f"La suma es: {suma}")
	except ValueError:
		messagebox.showerror("Error", "Por favor, ingrese números enteros válidos.")		
		
root = tk.Tk()
root.title("Suma")
root.geometry("700x400")

label1 = tk.Label(root, text="Ingrese el primer número:")	
label1.pack(pady=10)
entry1 = Entry(root)
entry1.pack(pady=10)	
label2 = tk.Label(root, text="Ingrese el segundo número:")
label2.pack(pady=10)
entry2 = Entry(root)
entry2.pack(pady=10)
button = ttk.Button(root, text="Sumar", command=suma)
button.pack(pady=20)
root.mainloop()