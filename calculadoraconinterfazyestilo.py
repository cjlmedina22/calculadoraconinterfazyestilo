import tkinter as tk
from tkinter import ttk
import math

# Variables globales
memoria = None
historial = []

# Funciones de la calculadora
def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: División por cero."

def exponente(x, y):
    return x ** y

def raiz_cuadrada(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo."

def factorial(x):
    return math.factorial(x)

def registrar_operacion(operacion, resultado):
    historial.append(f"{operacion} = {resultado}")

def mostrar_historial():
    historial_ventana = tk.Toplevel()
    historial_ventana.title("Historial de Operaciones")
    
    historial_texto = tk.Text(historial_ventana, wrap='word')
    historial_texto.pack(expand=True, fill='both')

    for operacion in historial:
        historial_texto.insert(tk.END, operacion + "\n")

    historial_texto.config(state='disabled')  # Hacer que el texto sea solo lectura

def guardar_historial():
    with open('historial.txt', 'w') as f:
        for operacion in historial:
            f.write(operacion + '\n')

def cargar_historial():
    global historial
    try:
        with open('historial.txt', 'r') as f:
            historial = f.readlines()
            historial = [operacion.strip() for operacion in historial]  # Eliminar saltos de línea
    except FileNotFoundError:
        print("No se encontró el archivo de historial. Se iniciará uno nuevo.")

# Clase para la interfaz gráfica
class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("400x500")
        
        self.resultado_var = tk.StringVar()
        self.resultado_var.set("0")

        self.crear_widgets()
        cargar_historial()  # Cargar historial al iniciar la aplicación

    def crear_widgets(self):
        # Pantalla de resultados
        pantalla = ttk.Entry(self, textvariable=self.resultado_var, font=("Arial", 24), justify='right')
        pantalla.grid(row=0, column=0, columnspan=4)

        # Botones
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('!', 5, 0), ('√', 5, 1), ('^', 5, 2), ('Historial', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('%', 6, 3)
        ]

        for (text, row, col) in botones:
            self.crear_boton(text, row, col)

    def crear_boton(self, texto, row, col):
        boton = ttk.Button(self, text=texto, command=lambda: self.on_boton_click(texto), width=10)
        boton.grid(row=row, column=col, padx=5, pady=5)

    def on_boton_click(self, texto):
        if texto == '=':
            try:
                # Resolver la expresión aritmética
                resultado = eval(self.resultado_var.get())
                self.resultado_var.set(resultado)
                registrar_operacion(self.resultado_var.get(), resultado)  # Registrar en el historial
                guardar_historial()  # Guardar en archivo
            except Exception as e:
                self.resultado_var.set("Error")
        elif texto == 'C':
            self.resultado_var.set("0")
        elif texto == '!':
            num = int(self.resultado_var.get())
            resultado = factorial(num)
            self.resultado_var.set(resultado)
            registrar_operacion(f"{num}!", resultado)  # Registrar en el historial
            guardar_historial()  # Guardar en archivo
        elif texto == '√':
            num = float(self.resultado_var.get())
            resultado = raiz_cuadrada(num)
            self.resultado_var.set(resultado)
            registrar_operacion(f"√{num}", resultado)  # Registrar en el historial
            guardar_historial()  # Guardar en archivo
        elif texto == 'sin':
            num = float(self.resultado_var.get())
            resultado = math.sin(math.radians(num))
            self.resultado_var.set(resultado)
            registrar_operacion(f"sin({num})", resultado)  # Registrar en el historial
            guardar_historial()  # Guardar en archivo
        elif texto == 'cos':
            num = float(self.resultado_var.get())
            resultado = math.cos(math.radians(num))
            self.resultado_var.set(resultado)
            registrar_operacion(f"cos({num})", resultado)  # Registrar en el historial
            guardar_historial()  # Guardar en archivo
        elif texto == 'tan':
            num = float(self.resultado_var.get())
            resultado = math.tan(math.radians(num))
            self.resultado_var.set(resultado)
            registrar_operacion(f"tan({num})", resultado)  # Registrar en el historial
            guardar_historial()  # Guardar en archivo
        elif texto == '%':
            num = float(self.resultado_var.get())
            resultado = num / 100
            self.resultado_var.set(resultado)
            registrar_operacion(f"{num}%", resultado)  # Registrar en el historial
            guardar_historial()  # Guardar en archivo
        else:
            if self.resultado_var.get() == "0":
                self.resultado_var.set(texto)
            else:
                self.resultado_var.set(self.resultado_var.get() + texto)

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
