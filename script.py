import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.font import Font

#Configuración basica
ventana = tkinter.Tk()
ventana.geometry("600x400")
ventana.title("Calculadora IMC")
ventana.configure(background = "#9b9b9b")

#Configuración fuentes
FuenteTitulo = Font(family = "Montserrat", size = 27, weight = "bold")
FuenteContexto = Font(family = "Montserrat",size = 12, weight = "normal")
FuenteVentana = Font(family = "Montserrat", size = 16, weight= "normal")
FuenteSeleccion = Font(family= "Montserrat", size = 14, weight= "normal")

#Color
ColorCaja = "#c4d2e7"

#Canva
frame = tkinter.Frame(ventana, width=460, height=200)
frame.place(x = 70, y = 140)
frame.config(bg= ColorCaja)
frame.config(bd=25, relief="solid", borderwidth=4)

#Titulo
Titulo = tkinter.Label(ventana, text = "Calculadora de IMC", font=FuenteTitulo, background = "#9b9b9b")
Titulo.place(x = 142, y = 20)

#Descripción
Contexto = tkinter.Label(ventana, text = "Descubre tu indice IMC para saber si estas como una vaca (o no)", background = "#9b9b9b", font = FuenteContexto)
Contexto.place(x=77,y=65)

#Edad y genero
Genero = tkinter.Label(ventana, text = "Género", font= FuenteVentana, bg = ColorCaja)
Genero.place(x=95, y=165)
GeneroElegir = ttk.Combobox(ventana, state="readonly", values=["Hombre", "Mujer"], width= 8, font=FuenteSeleccion)
GeneroElegir.place(x = 180, y = 166)

ventana.mainloop()