from tkinter import ttk
import tkinter as tk
import sys
import os.path
from tkinter import scrolledtext as st

class Modelo:
        __arrNombres,__cadena = [],None
        def __init__(self):
            pass


def analisisCadena(text1):
    arrcadena = []
    print (text1.get("1.0", tkinter .END))
    cadena=text1.get("1.0", tkinter .END)
    arrcadena = cadena.split("\n")
    # arrNombres = cadena.split("class ")
    # arrNombres.remove("")
    # arrNombres = cadena.split("class ")
    arrcadena.remove("")
    # print(arrcadena)
    for i in range(len(arrcadena)):
        if "class " in arrcadena[i]:
            nombreClase = arrcadena[i]
        if "__" in arrcadena[i]:
            arratributos = arrcadena[i].split("__")

    print()
    print(nombreClase)
    print(arrcadena)






class Vista():
        __marco,__canvas,__lados,__radio = None,None,None,None
        def __init__(self):
            self.__marco = tk.Tk()
            self.__marco.geometry("800x800")
            self.__marco.title("Diagrrama de clases")
            #self.__canvas = tk.Text(self.__marco,width=164, height=94, bg='white')
            #self.__canvas.place(x=100, y = 14)


        def mostrar(self):
                #Labels
                self.__l1 = tk.Label(self.__marco, text = "Nombre de la clase:")
                self.__l1.place(x=10, y=14)
                self.__l2 = tk.Label(self.__marco, text = "Nombre del atributo: ")
                self.__l2.place(x=10 , y=74)
                self.__l3 = tk.Label(self.__marco, text = "Nombre del metodo: ")
                self.__l3.place(x=10, y=169)
                self.__l4 = tk.Label(self.__marco, text="Relacion: ")
                self.__l4.place(x=10, y=320)
                #self.__l5 = tk.Label(self.__marco, text="Cardinalidad: ")
                #self.__l5.place(x=10, y=420)

                #Entrys
                self.__nombreClase = tk.Entry(self.__marco)
                self.__nombreClase.place(x=130, y=10)
                self.__nombreClase.config(width=30)
                self.__nombreAtributo = tk.Entry(self.__marco)
                self.__nombreAtributo.place(x=130, y=70)
                self.__nombreAtributo.config(width=30)
                self.__nombreMetodo = tk.Entry(self.__marco)
                self.__nombreMetodo.place(x=130, y=170)
                self.__nombreMetodo.config(width=30)

                #Comboboxes
                self.__tipoClase = ttk.Combobox(self.__marco, state="readonly")
                self.__tipoClase.place(x=10, y=38)
                self.__tipoClase.config(width=10)
                self.__tipoClase["values"] = ["__", ""]
                self.__tipoAtributo = ttk.Combobox(self.__marco, state="readonly")
                self.__tipoAtributo.place(x=10, y=100)
                self.__tipoAtributo.config(width=10)
                self.__tipoAtributo["values"] = ["__", ""]
                self.__tipoMetodo = ttk.Combobox(self.__marco, state="readonly")
                self.__tipoMetodo.place(x=10, y=192)
                self.__tipoMetodo.config(width=10)
                self.__tipoMetodo["values"] = ["__", ""]
                self.__Relacion1 = ttk.Combobox(self.__marco, state="readonly")
                self.__Relacion1.place(x=10, y=340)
                self.__Relacion1.config(width=15)
                #self.__Relacion1["values"] = ["__", ""]
                self.__TipoRelacion = ttk.Combobox(self.__marco, state="readonly")
                self.__TipoRelacion.place(x=155, y=340)
                self.__TipoRelacion.config(width=12)
                self.__TipoRelacion["values"] = ["extends", "implements"]
                self.__Relacion2 = ttk.Combobox(self.__marco, state="readonly")
                self.__Relacion2.place(x=270, y=340)
                self.__Relacion2.config(width=15)

                self.__marco.mainloop()

        def dev_canvas(self):
                return self.__canvas

        def dev_txt(self):
            return 0

        def eventoBton(self,controlador):
            self.__btnRegistrarClase = tk.Button(self.__marco, text="Registrar clase")#, command=lambda: analisisCadena(self.text1))
            self.__btnRegistrarClase.place(x=130, y=40)
            self.__btnRegistrarClase.config(width = 20)
            self.__btnRegistrarAtributo = tk.Button(self.__marco, text="Registrar atributo")  # , command=lambda: analisisCadena(self.text1))
            self.__btnRegistrarAtributo.place(x=130, y=110)
            self.__btnRegistrarAtributo.config(width=20)
            self.__btnRegistrarMetodo = tk.Button(self.__marco, text="Registrar metodo")  # , command=lambda: analisisCadena(self.text1))
            self.__btnRegistrarMetodo.place(x=130, y=200)
            self.__btnRegistrarMetodo.config(width=20)
            self.__btnFinalizarClase = tk.Button(self.__marco, text="Finalizar clase")  # , command=lambda: analisisCadena(self.text1))
            self.__btnFinalizarClase.place(x=130, y=270)
            self.__btnFinalizarClase.config(width=20)
            self.__btnCrearRelacion = tk.Button(self.__marco, text="Crear relacion")  # , command=lambda: analisisCadena(self.text1))
            self.__btnCrearRelacion.place(x=140, y=380)
            self.__btnCrearRelacion.config(width=20)
            self.__btnCrearCardinalidad = tk.Button(self.__marco, text="Crear cardinalidad")  # , command=lambda: analisisCadena(self.text1))
            self.__btnCrearCardinalidad.place(x=140, y=420)
            self.__btnCrearCardinalidad.config(width=20)
            self.__btnDiagramaUML = tk.Button(self.__marco, text="Diagrama UML")  # , command=lambda: analisisCadena(self.text1))
            self.__btnDiagramaUML.place(x=140, y=460)
            self.__btnDiagramaUML.config(width=20)


class controlador:
        def __init__(self):
                pass
        def asignar(self,m,v):
                self.__modelo=m
                self.__vista = v
m= Modelo()
v = Vista()
control = controlador()
control.asignar(m,v)
v.eventoBton(control)
v.mostrar()