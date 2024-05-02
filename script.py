#Importar Librerias
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.font import Font

#Configuración basica
ventana = tkinter.Tk()
ventana.geometry("600x400")
ventana.title("Calculadora IMC")
ventana.configure(background = "#9b9b9b")

#Configuración menú
barra_menus = tkinter.Menu()
menu_archivo = tkinter.Menu(barra_menus, tearoff=False)
menu_archivo.add_command(
    label="Nuevo",
    accelerator="Ctrl+N",
    compound=tkinter.LEFT
)
barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
ventana.config(menu=barra_menus)


#Configuración fuentes
FuenteTitulo = Font(family = "Montserrat", size = 27, weight = "bold")
FuenteContexto = Font(family = "Montserrat",size = 12, weight = "normal")
FuenteVentana = Font(family = "Montserrat", size = 16, weight= "normal")
FuenteSeleccion = Font(family= "Montserrat", size = 14, weight= "normal")
FuenteResultado = Font(family = "Montserrat", size = 18, weight= "normal")

#Configuración Colores
ColorCaja = "#c4d2e7"

#Función Principal
def Calcular():
    P = int(PesoElegir.get())
    A = float(AlturaElegir.get())
    AA = A*A
    Resultado = P/AA
    print(Resultado)
    ResultadoTexto = tkinter.StringVar()
    ResultadoTexto.set(f"Tu IMC es de " + str(Resultado))
    TextoResultado = tkinter.Label(ventana, textvariable=ResultadoTexto, font=FuenteResultado)
    TextoResultado.place(x = 220, y = 350)

#Fondo
frame = tkinter.Frame(ventana, width=460, height=200)
frame.place(x = 70, y = 140)
frame.config(bg= ColorCaja)
frame.config(bd=25, relief="solid", borderwidth=4)

#Titulo
Titulo = tkinter.Label(ventana, text = "Calculadora de IMC", font=FuenteTitulo, background = "#9b9b9b").place(x = 142, y = 20)

#Descripción
Contexto = tkinter.Label(ventana, text = "Descubre tu indice IMC para saber si estas como una vaca (o no)", background = "#9b9b9b", font = FuenteContexto).place(x=77,y=65)

#Peso
Peso = tkinter.Label(ventana, text = "Peso", font = FuenteVentana, bg= ColorCaja).place(x=103, y = 180)
PesoElegir = tkinter.Entry(ventana,width=10, font = FuenteSeleccion)
PesoElegir.place(x=165, y= 180)


#Altura
Altura = tkinter.Label(ventana, text = "Altura",font = FuenteVentana, bg = ColorCaja).place(x=320, y = 180)
AlturaElegir = tkinter.Entry(ventana, width=10, font = FuenteSeleccion)
AlturaElegir.place(x=385, y= 180)


#Botón
Boton = ttk.Button(ventana, text = "Calcula", width = 20,command= Calcular).place(x = 234, y = 230)


ventana.mainloop()