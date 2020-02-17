from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from mysql.connector import Error


def cerrar(marco):
    marco.destroy()


def crearBase():
    nombre = campo1.get()
    mydb = mysql.connector.connect(host="localhost", user="root", password="Sebastian1996")
    micursor = mydb.cursor()
    comando = "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = %s"
    micursor.execute(comando, (nombre,))
    resultado = micursor.fetchone()
    if resultado == None:
        comando = "create database " + nombre
        micursor.execute(comando)
        messagebox.showinfo("Base Creada", "Base creada exitosamente con el nombre: " + nombre)

    if resultado != None:
        messagebox.showwarning("Base existente", "Ya existe el nombre usado, por favor intente nuevamente")
    micursor.close()
    mydb.close()


def crearTabla():
    tabla = campoTabla.get()
    base = campo1.get()
    mydb = mysql.connector.connect(host="localhost", user="root", password="Sebastian1996", database=base)
    micursor = mydb.cursor()
    micursor.execute(
        "CREATE TABLE IF NOT EXISTS " + tabla + "(codigo VARCHAR(20) NOT NULL PRIMARY KEY, nombre VARCHAR(20) NOT NULL, nota1 DOUBLE, nota2 DOUBLE, nota3 DOUBLE)")
    micursor.close()
    mydb.close()
    messagebox.showinfo("Tabla Creada", "Tabla creada exitosamente con el nombre: " + tabla)


def registrarEstudiante():
    mydb = mysql.connector.connect(host="localhost", user="root", password="Sebastian1996", database=campo1.get())
    micursor = mydb.cursor()
    cod = campoCodigo.get()
    comando = "SELECT * FROM estudiantes WHERE codigo=%s"
    micursor.execute(comando, (cod,))
    micursor.fetchone()
    if micursor.rowcount > 0:
        messagebox.showwarning("Estudiante existente",
                               "Ya existe el estudiante " + cod + ", por favor intente nuevamente")
        micursor.close()
        mydb.close()
    else:
        nom = campoEstudiante.get()
        nota1 = float(campoNota1.get())
        nota2 = float(campoNota2.get())
        nota3 = float(campoNota3.get())
        comando2 = "INSERT INTO estudiantes(codigo, nombre, nota1, nota2, nota3) VALUES(%s, %s, %s, %s, %s)"
        micursor.execute(comando2, (cod, nom, nota1, nota2, nota3))
        mydb.commit()
        micursor.close()
        mydb.close()
        messagebox.showinfo("Registro exitoso", "Estudiante " + cod + " registrado exitosamente")


def eliminarEstudiante():
    mydb = mysql.connector.connect(host="localhost", user="root", password="Sebastian1996",
                                   database=campo1.get())
    try:
        micursor = mydb.cursor()
        if cbCodigoyEst.get() == "Codigo":
            cod = campoCodigo.get()
            comando = "DELETE FROM estudiantes WHERE codigo=%s"
            micursor.execute(comando, (cod,))
            mydb.commit()
            messagebox.showinfo("Estudiante Eliminado", "Estudiante exitosamente eliminado")

        elif cbCodigoyEst.get() == "Estudiante":
            nom = campoEstudiante.get()
            comando = "DELETE FROM estudiantes WHERE nombre=%s"
            micursor.execute(comando, (nom,))
            mydb.commit()
            messagebox.showinfo("Estudiante Eliminado", "Estudiante exitosamente eliminado")
            micursor.close()
            mydb.close()
    except Error as e:
        messagebox.showerror("Error", "Error en la base de datos, o estudiante selecionados")


def buscarEstudiante():
    mydb = mysql.connector.connect(host="localhost", user="root", password="Sebastian1996",
                                   database=campo1.get())
    try:
        micursor = mydb.cursor()
        if cbCodigoyEst.get() == "Codigo":
            cod = campoCodigo.get()
            comando = "SELECT * FROM estudiantes WHERE codigo=%s"
            micursor.execute(comando, (cod,))
            resultado = micursor.fetchone()
            if resultado == None:
                messagebox.showwarning("Estudiante no encontrado", "No hay ningun estudiante con ese codigo")
                micursor.close()
                mydb.close()
            if resultado != None:
                messagebox.showinfo("Estudiante", str(resultado))
        elif cbCodigoyEst.get() == "Estudiante":
            nom = campoEstudiante.get()
            comando = "SELECT * FROM estudiantes WHERE nombre=%s"
            micursor.execute(comando, (nom,))
            resultado = micursor.fetchone()
            if resultado == None:
                messagebox.showwarning("Estudiante no encontrado", "No hay ningun estudiante con ese codigo")
            if resultado != None:
                messagebox.showinfo("Estudiante", str(resultado))
            micursor.close()
            mydb.close()
    except Error as e:
        messagebox.showerror("Error", "Error en la base de datos, o estudiante selecionados")


def actualizarNotas():
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="Sebastian1996", database=campo1.get())
        micursor = mydb.cursor()
        cod = campoCodigo.get()
        if cbNotas.get() == "Nota 1":
            auxNota = float(campoNota1.get())
            comando = "UPDATE estudiantes SET nota1=%s WHERE codigo=%s"
            micursor.execute(comando, (auxNota, cod))
            mydb.commit()
            messagebox.showinfo("Registro actualizado", "Nota1 actualizada")
        if cbNotas.get() == "Nota 2":
            auxNota = float(campoNota2.get())
            comando = "UPDATE estudiantes SET nota2=%s WHERE codigo=%s"
            micursor.execute(comando, (auxNota, cod))
            mydb.commit()
            messagebox.showinfo("Registro actualizado", "Nota 2 actualizada")
        if cbNotas.get() == "Nota 3":
            auxNota = float(campoNota3.get())
            comando = "UPDATE estudiantes SET nota3=%s WHERE codigo=%s"
            micursor.execute(comando, (auxNota, cod))
            mydb.commit()
            messagebox.showinfo("Registro actualizado", "Nota 3 actualizada")
    except Error as e:
        messagebox.showerror("Error", "Error en la base de datos, o estudiante selecionados")
    micursor.close()
    mydb.close()


def verTabla():
    top = Toplevel()
    top.geometry("700x300")
    top.resizable(width=None, height=None)
    text = Text(top)
    scroll = Scrollbar(top, command=text.yview)
    text.pack(side=LEFT)
    scroll.pack(side=RIGHT, fill=Y)
    mydb = mysql.connector.connect(host="localhost", user="root", password="Sebastian1996", database="BaseEstudiantes")
    try:
        comando3 = "SELECT * FROM estudiantes"
        micursor = mydb.cursor()
        micursor.execute(comando3)
        registros = micursor.fetchall()
        promedio = 0
        text.insert(END,
                    "{:15s} {:20s} {:10s} {:10s} {:10s} {:10s}".format("Codigo", "Nombre", "Nota 1", "Nota 2", "Nota 3",
                                                                       "Promedio"))
        for fila in registros:
            text.insert(END,"{:15s} {:20s} {:10f} {:10f} {:10f} {:10f}".format(fila[0],fila[1],fila[2], fila[3], fila[4], (fila[2]+fila[3]+fila[4])/3))
            promedio = promedio+((fila[2]+fila[3]+fila[4])/3)
        text.insert(END,"Promedio del curso: " + str(promedio / micursor._rowcount))
        micursor.close()
        mydb.close()
    except Error as e:
        print("error")


marco = Tk()
marco.title("Base de Datos")
marco.geometry('700x600')
marco.configure(background='#A1A8D8')

campo1 = Entry()
campo1.place(x=400, y=20)
label1 = Label(marco, text="Base de datos", bg='#A1A8D8')
label1.place(x=300, y=20)
botonCrearBase = Button(marco, text="Crear base de datos", command=lambda: crearBase())
botonCrearBase.place(x=10, y=20)
botonCrearBase.config(font=("Consolas", 12), pady=5)

boton = Button(marco, text="Crear Tablas", command=lambda: crearTabla())
boton.place(x=10, y=80)
boton.config(font=("Consolas", 12), pady=5)
campoTabla = Entry()
campoTabla.place(x=400, y=60)
label2 = Label(marco, text="Tabla: ", bg='#A1A8D8')
label2.place(x=300, y=60)

botonrstudent = Button(marco, text="Registrar Estudiante", command=lambda: registrarEstudiante())
botonrstudent.place(x=10, y=140)
campoCodigo = Entry()
campoCodigo.place(x=400, y=100)
campoEstudiante = Entry()
campoEstudiante.place(x=400, y=140)
campoNota1 = Entry()
campoNota1.place(x=400, y=180)
campoNota2 = Entry()
campoNota2.place(x=400, y=220)
campoNota3 = Entry()
campoNota3.place(x=400, y=260)
label3 = Label(marco, text="Codigo: ", bg='#A1A8D8')
label3.place(x=300, y=100)
label4 = Label(marco, text="Estudiante: ", bg='#A1A8D8')
label4.place(x=300, y=140)
label5 = Label(marco, text="Nota 1: ", bg='#A1A8D8')
label5.place(x=300, y=180)
label6 = Label(marco, text="Nota 2: ", bg='#A1A8D8')
label6.place(x=300, y=220)
label7 = Label(marco, text="Nota 3: ", bg='#A1A8D8')
label7.place(x=300, y=260)
cbCodigoyEst = ttk.Combobox(marco, state="readonly")
cbCodigoyEst["values"] = ["Codigo", "Estudiante"]
cbCodigoyEst.place(x=550, y=99)
botonrstudent.config(font=("Consolas", 12), pady=5)

botonlc = Button(marco, text="Listar curso", command=lambda: verTabla())
botonlc.place(x=10, y=200)
botonlc.config(font=("Consolas", 12), pady=5)

botonfs = Button(marco, text="Buscar Estudiante", command=lambda: buscarEstudiante())
botonfs.place(x=10, y=260)
botonfs.config(font=("Consolas", 12), pady=5)

botonrd = Button(marco, text="Actualizar datos", command=lambda: actualizarNotas())
botonrd.place(x=10, y=320)
botonrd.config(font=("Consolas", 12), pady=5)
cbNotas = ttk.Combobox(marco, state="readonly")
cbNotas["values"] = ["Nota 1", "Nota 2", "Nota 3"]
cbNotas.place(x=550, y=139)

botonds = Button(marco, text="Eliminar Estudiante", command=lambda: eliminarEstudiante())
botonds.place(x=10, y=380)
botonds.config(font=("Consolas", 12), pady=5)

b_cerrar = Button(marco, text='Cerrar', command=cerrar)
b_cerrar.place(x=10, y=440)
b_cerrar.config(font=("Consolas", 12), pady=5)

marco.mainloop()
