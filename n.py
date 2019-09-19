import tkinter as tk
from tkinter import *
import tkinter, sys
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
            print(arratributos)
    print(nombreClase)
    print(arrcadena)







class Vista():
        __marco,__canvas,__lados,__radio = None,None,None,None
        def __init__(self):
            self.__marco = tk.Tk()
            self.__marco.geometry("800x800")
            self.__marco.title("Diagrrama de clases")
            self.__canvas = tk.Canvas(self.__marco,width=300, height=300, bg='white')
            self.__canvas.place(x=400, y = 120)


        def mostrar(self):
                self.text1 = st.ScrolledText(self.__marco, width=40, height=10)
                self.text1.place(x=20, y=120)

                self.__l1 = tk.Label(self.__marco, text = "Bienvenido a la Diagramacion de clases ")
                self.__l1.place(x=100 , y=20)
                self.__l1.config(fg="blue", bg='#f2f2d4', font=("Verdana", 19))

                self.__marco.mainloop()
        def dev_canvas(self):
                return self.__canvas

        def dev_txt(self):
            return 0
        def eventoBton(self,controlador):
                self.__boton = tk.Button(self.__marco,text="Crear nueva Clase ", command=lambda: analisisCadena(self.text1))
                self.__boton.place(x=20, y=80)


class controlador:
        def __init__(self):
                pass
        def asignar(self,m,v):
                self.__modelo=m
                self.__vista = v


class vista2():
    __x , __y = None, None
    def __init__(self):
        self.__marco = tk.Tk()
        self.__marco.geometry("800x800")
        self.__marco.title("Diagrrama de clases")
        self.__canvas = tk.Canvas(self.__marco, width=300, height=300, bg='white')
        self.__canvas.place(x=0, y=0)
        self.__canvas.pack(fill=BOTH,expand=YES)

    def cuadrado(self,clase,atributos,metodos):

        y = int(len(atributos))*10
        y2 = int(len(metodos))*10
        posx1 = 10
        posx2 = 80
        posy2 = 30
        self.__c= self.__canvas.create_rectangle(posx1,posx1,posx2,posy2)
        self.__c2= self.__canvas.create_rectangle(posx1,posx1,posx2,posy2+y)
        self.__c3 = self.__canvas.create_rectangle(posx1, posx1, posx2, posy2+y+y2)
        self.__nc=self.__canvas.create_text(15,15,fill="darkblue",
                        text=clase,anchor=NW)
        for i in range(len(atributos)):
            self.__canvas.create_text(15, 15, fill="darkblue",
                                      text=clase, anchor=NW)


    def nombreClase(self,n,clase):
        y = 0
        for i in range(n):
            self.__c= self.__canvas.create_rectangle(10,10+y,80,80+y)
    def mostrar(self):
        atributos = [1, 2, 3, 4, 5]
        metodos = [1, 2, 3, 4, 5]
        clase = "class a"
        self.cuadrado(clase, atributos,metodos)
        self.__marco.mainloop()

    def dev_marco(self):
        return self.__marco



    def dev_canvas(self):
        return self.__canvas


m= Modelo()
v = vista2()
control = controlador()
control.asignar(m,v)
# v.eventoBton(control)
v.mostrar()