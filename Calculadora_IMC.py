import tkinter as tk
from tkinter import ttk

# Creamos la interfaz grafica
ventana = tk.Tk()
ventana.title("Calculador de Masa Corporal")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="Inrgese su altura (metros)")
etiqueta.pack()

EntradaAltura = tk.Entry(ventana, width=30)
EntradaAltura.pack(pady=10)

etiqueta2 = tk.Label(ventana, text="Ingrese su peso (kg)")
etiqueta2.pack()

EntradaPeso = tk.Entry(ventana, width=30)
EntradaPeso.pack(pady=10)

Resultado = tk.Label(ventana, text="")
Resultado.pack()

ClasificacionPeso = tk.Label(text="")
ClasificacionPeso.pack()

#IMC = peso / (altura × altura)

# Calculamos el indice de masa corporal con el peso y la altura
def Calcular():

    try:

        # Obtenemos los datos de los labels
        Peso = float(EntradaPeso.get())
        Altura = float(EntradaAltura.get())

        # Si la altura y el peso no son validos mostrar un mensaje
        if Altura < 1.00:
            Resultado.config(text="Ingrese una altura valida")
            return
        
        if Peso < 50:
            Resultado.config(text="Ingrese un peso valido")
            return
        
        masa_corporal = Peso / (Altura * Altura)
        # Redondeamos el valor y que muestre 2 decimales
        masa_corporal_redondeada = round(masa_corporal,2)

        Resultado_texto = "Su masa corporal es: " + str(masa_corporal_redondeada)
        Resultado.config(text=Resultado_texto)

        # Clasificacion de masa corporal
        if masa_corporal_redondeada < 18.5: 
                ClasificacionPeso.config(text="Usted tiene bajo peso")

        elif masa_corporal_redondeada > 18.5 and masa_corporal_redondeada < 24.9:
             ClasificacionPeso.config(text="Usted tiene peso normal(saludable)")

        elif masa_corporal_redondeada > 25.0 and masa_corporal_redondeada < 29.9:
             ClasificacionPeso.config(text="Usted tiene sobrepeso")
            
        elif masa_corporal_redondeada > 30.0 and masa_corporal_redondeada < 24.9:
             ClasificacionPeso.config(text="Usted tiene obesidad grado 1")

        elif masa_corporal_redondeada > 25.0 and masa_corporal_redondeada < 39.9:
             ClasificacionPeso.config(text="Usted tiene obesidad grado 2")

        elif masa_corporal_redondeada > 40.0:
             ClasificacionPeso.config(text="Usted tiene obesidad grado 3")
        
    except ValueError:
        Resultado.config(text="Ingrese un valor")

     
Boton = tk.Button(ventana, text="Calcular", command=Calcular, bg="grey")
Boton.pack()

ventana.mainloop()