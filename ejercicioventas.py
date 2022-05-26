#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox
import sqlite3


with sqlite3.connect("ventas.sqlite") as con:
    cursor = con.cursor()
    try:
        cursor.execute("create table ventas (ID integer primary key autoincrement, producto text, precio float)")
    except:
        pass



def ingresar():
    producto = caja1.get()
    precio = caja2.get()
    
    if producto=="" or precio=="":
        messagebox.showwarning("Atención", "Hay que completar ambos campos")
        return
    
    precio = precio.replace(",", ".")
    try:
        precio = float(precio)
    except:
        messagebox.showwarning("Atención", "El precio debe ser un número")
        return
    
    
    with sqlite3.connect("ventas.sqlite") as con:
        cursor = con.cursor()
        cursor.execute("insert into ventas values (null, ?, ?)", (producto, precio))
    
    caja1.delete(0, tk.END)
    caja2.delete(0, tk.END)
    
    
def suma():
    with sqlite3.connect("ventas.sqlite") as con:
        cursor = con.cursor()
        cursor.execute("select sum(precio) from ventas")
        (suma,) = cursor.fetchone()
        
        total.set("$ {}".format(suma))



def mostrar():
    with sqlite3.connect("ventas.sqlite") as con:
        cursor = con.cursor()
        cursor.execute("select * from ventas")
        registros = cursor.fetchall()
        
        s = ""
        for ID, producto, precio in registros:
            s = s + "{:4d} - {:20s} ${:8.2f}\n".format(ID, producto, precio)
        
        
        mensaje.set(s)







ventana = tk.Tk()
ventana.title("Gestión de ventas")
ventana.config(width=800, height=700)



etiqueta1 = tk.Label(text="Ingreso de Ventas")
etiqueta1.place(x=80,y=80)
etiqueta1.config(font=("",15))


etiqueta2 = tk.Label(text="Producto")
etiqueta2.place(x=100, y=120)

caja1 = tk.Entry()
caja1.place(x=200, y=120)


etiqueta3 = tk.Label(text="Precio")
etiqueta3.place(x=100, y=150)

caja2 = tk.Entry()
caja2.place(x=200, y=150)

boton1 = tk.Button(text="Ingresar venta", command=ingresar)
boton1.place(x=350, y=135)





boton2 = tk.Button(text="Mostrar total de ventas", command=suma)
boton2.place(x=80, y=250)

total = tk.StringVar()
etiqueta4 = tk.Label(textvariable=total)
etiqueta4.place(x=280, y=250)
etiqueta4.config(font=("", 15))


boton3 = tk.Button(text="Mostrar las ventas", command=mostrar)
boton3.place(x=80, y=330)

mensaje = tk.StringVar()
etiqueta5 = tk.Label(textvariable=mensaje, justify="left")
etiqueta5.place(x=230, y=330)
etiqueta5.config(font=("Consolas",10))



ventana.mainloop()




































