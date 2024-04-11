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
FuenteTitulo = Font(family = "Montserrat", size = 26, weight = "bold")
FuenteContexto = Font(family = "Montserrat",size = 13, weight = "normal" )

#Titulo
Titulo = tkinter.Label(ventana, text = "Calculadora de IMC", font=FuenteTitulo, background = "#9b9b9b")
Titulo.place(x = 142, y = 20)

#Descripción
Contexto = tkinter.Label(ventana, text = "Descubre tu indice IMC para saber si estas como una vaca (o no)", background = "#9b9b9b", font = FuenteContexto)
Contexto.place(x=63,y=65)

ventana.mainloop()