from tkinter import *
import math as m
i=0
e=0
#Funciones

def click(valor):
    global i
    global e
    e_texto.insert(i,valor)
    e1_texto.insert(e,valor)
    i+=1
    e+=1

def borrar():
    global i
    global e
    e_texto.delete(0,END)
    e1_texto.delete(0,END)
    i=0
    e=0

def log():
    global i
    global e
    e_texto.insert(i,"m.log10")
    e1_texto.insert(e,"log")
    i+=7
    e+=3

def ln():
    global i
    global e
    e_texto.insert(i,"m.log")
    e1_texto.insert(e,"Ln")
    i+=5
    e+=2

def igual():
    global i
    global e
    ecuacion=e_texto.get()
    e_texto.delete(0,END)
    e1_texto.delete(0,END)
    resultado=eval(ecuacion)
    e_texto.insert(0,resultado)
    e1_texto.insert(0,resultado)
    i=len(str(resultado))
    e=len(str(resultado))

def raiz():
    global i
    global e
    e_texto.insert(i,"m.sqrt")
    e1_texto.insert(e,chr(5920))
    i+=6
    e+=1

def pot():
    global i
    global e
    e_texto.insert(i,"**")
    e1_texto.insert(e,"^")
    i+=2
    e+=1

def Pi():
    global i
    global e
    e_texto.insert(i,"m.pi")
    e1_texto.insert(e, chr(8508))
    i=i+4
    e+=2

def mul():
    global i
    global e
    e_texto.insert(i,"*")
    e1_texto.insert(e, chr(8226))
    i+=1
    e+=1

def Borrar():
    global i
    global e
    texto=e_texto.get()
    largo=len(texto)

    if (largo>=1 and texto[i-1]=="i"):
        e_texto.delete(i-4,END)
        i-=4
        e1_texto.delete(e-2,END)
        e-=2
        return

    if(largo>=1 and texto[i-1]== "t"):
        e_texto.delete(i-6,END)
        i-=6
        e1_texto.delete(e-1,END)
        e-=1
        return

    if(largo>=2 and texto[i-2]== "*" and texto[i-1]== "*"):
        e_texto.delete(i-2,END)
        i-=2
        e1_texto.delete(e-1,END)
        e-=1
        return

    if(largo>=3 and texto[i-3]== "g" and texto[i-2]== "1" and texto[i-1]== "0"):
        e_texto.delete(i-7,END)
        i-=7
        e1_texto.delete((e-3),END)
        e-=3
        return

    if(largo>=1 and texto[i-1] == "g"):
        e_texto.delete(i-5,END)
        i-=5
        e1_texto.delete(e-2,END)
        e-=2
        return
    
    if(largo>=1 and texto[i-1] == "n"):
        e_texto.delete(i-5,END)
        i-=5
        e1_texto.delete(e-3,END)
        e-=3
        return

    if(largo>=1 and texto[i-1] == "s"):
        e_texto.delete(i-5,END)
        i-=5
        e1_texto.delete(e-3,END)
        e-=3
        return

    if(largo>=1 and texto[i-1] == "e"):
        e_texto.delete(i-3,END)
        i-=3
        e1_texto.delete(e-1,END)
        e-=1
        return

    else:
        e_texto.delete(i-1,END)
        i-=1
        e1_texto.delete(e-1,END)
        e-=1

def Div():
    global i
    global e
    e_texto.insert(i,"/")
    e1_texto.insert(e,"/")
    i+=2
    e+=2

def seno():
    global i
    global e
    e_texto.insert(i,"m.sin")
    e1_texto.insert(e,"sen")
    i+=5
    e+=3

def coseno():
    global i
    global e
    e_texto.insert(i,"m.cos")
    e1_texto.insert(e,"cos")
    i+=5
    e+=3

def tangente():
    global i
    global e
    e_texto.insert(i,"m.tan")
    e1_texto.insert(e,"tan")
    i+=5
    e+=3

def euler():
    global i
    global e
    e_texto.insert(i,"m.e")
    e1_texto.insert(e,"e")
    i+=3
    e+=1

#Ventana 

ventana =Tk()
ventana.title(chr(3476)+" Calculadora "+chr(3476))
ventana.attributes("-fullscreen", False)
ventana["bg"]="gray16"
ventana.geometry("330x290")
ventana.iconbitmap("C:/Users/Amaro/OneDrive/Escritorio/pruebas/7007513_finance_calculator_accounting_business_icon.ico")

#Entrada
e_texto = Entry(ventana, font= ("Times"), background="gray16" ,foreground= "snow", width= 32)
e1_texto= Entry(ventana, font= ("Times"), background="gray16" ,foreground= "snow", width= 32)
e1_texto.grid(row =0, column = 0, columnspan = 6, padx= 2, pady= 5)

#Botones

boton1 = Button(ventana, text = "1", width= 5, height= 2, background="gray33", foreground="snow", command= lambda: click(1))
boton2 = Button(ventana, text = "2", width= 5, height= 2, background="gray33", foreground="snow", command= lambda: click(2))
boton3 = Button(ventana, text = "3", width= 5, height= 2, background="gray33", foreground="snow", command= lambda: click(3))
boton4 = Button(ventana, text = "4", width= 5, height= 2, background="gray33", foreground="snow", command= lambda: click(4))
boton5 = Button(ventana, text = "5", width= 5, height= 2, background="gray33", foreground="snow", command= lambda: click(5))
boton6 = Button(ventana, text = "6", width= 5, height= 2, background="gray33", foreground="snow", command= lambda: click(6))
boton7 = Button(ventana, text = "7", width= 5, height= 2, background="gray33", foreground="snow", command= lambda: click(7))
boton8 = Button(ventana, text = "8", width= 5, height= 2, background="gray33", foreground="snow", command= lambda: click(8))
boton9 = Button(ventana, text = "9", width= 5, height= 2, background="gray33", foreground="snow", command= lambda: click(9))
boton0 = Button(ventana, text = "0", width= 13, height= 2, background="gray33", foreground="snow", command= lambda: click(0))

boton_sum = Button(ventana, text = "+", width= 5, height= 2, background="gray26", foreground="snow", command= lambda: click("+"))
boton_res = Button(ventana, text = "-", width= 5, height= 2, background="gray26", foreground="snow", command= lambda: click("-"))
boton_mul = Button(ventana, text = "x", width= 5, height= 2, background="gray26", foreground="snow", command= lambda: mul())
boton_div = Button(ventana, text=chr(247), width= 5, height= 2, background="gray26", foreground="snow", command= lambda: Div())

boton_igual = Button(ventana, text = "=", width= 5, height= 2, background="gray26", foreground="snow", command= lambda: igual())
boton_del = Button(ventana, text= "AC", width= 5, height= 2, background="gray26", foreground="snow", command= lambda: borrar())

boton_par1 = Button(ventana, text = "(", width= 5, height= 2, background="gray26", foreground="snow", command= lambda: click("("))
boton_par2 = Button(ventana, text = ")", width= 5, height= 2, background="gray26", foreground="snow", command= lambda: click(")"))
boton_punto = Button(ventana, text = ".", width= 5, height= 2, background="gray26", foreground="snow", command= lambda: click("."))

boton_pot = Button(ventana, text = "a " +  chr(879), width= 5, height= 2, background="gray26", foreground="snow", command= lambda: pot())
boton_raiz = Button(ventana, text = chr(5920), width= 5, height= 2, background="gray26", foreground="snow", command= lambda: raiz())
boton_log = Button(ventana, text = "log", width= 5, height= 2, background="gray26", foreground="snow", command= lambda: log())
boton_ln = Button(ventana, text = "Ln", width= 5, height= 2, background="gray26", foreground="snow", command= lambda: ln())
boton_pi = Button(ventana, text = "Pi", width= 5, height= 2, background="gray26", foreground="snow", command= lambda: Pi())

boton_Borrar = Button(ventana, text = chr(9003), width= 5, height= 2, background="gray26", foreground="snow", command= lambda: Borrar())
boton_sen = Button(ventana, text = "sen", width= 5, height= 2, background="gray26", foreground="snow", command= lambda: seno())
boton_cos = Button(ventana, text = "cos", width= 5, height= 2, background="gray26", foreground="snow", command= lambda: coseno())
boton_tan = Button(ventana, text = "tan", width= 5, height= 2, background="gray26", foreground="snow", command= lambda: tangente())
boton_euler = Button(ventana, text = "e", width= 5, height= 2, background="gray26", foreground="snow", command= lambda: euler())

#Agregar botones en pantalla


boton_del.grid(row= 1, column= 0, padx= 5, pady=5)
boton_par1.grid(row= 1, column= 1, padx= 5, pady=5)
boton_par2.grid(row= 1, column= 2, padx= 5, pady=5)
boton_div.grid(row= 1, column= 4, padx= 5, pady=5)

boton9.grid(row= 2, column= 3, padx= 5, pady=5)
boton8.grid(row= 2, column= 2, padx= 5, pady=5)
boton7.grid(row= 2, column= 1, padx= 5, pady=5)
boton_mul.grid(row= 2, column= 4, padx= 5, pady=5)

boton6.grid(row= 3, column= 3, padx= 5, pady=5)
boton5.grid(row= 3, column= 2, padx= 5, pady=5)
boton4.grid(row= 3, column= 1, padx= 5, pady=5)
boton_sum.grid(row= 3, column= 4, padx= 5, pady=5)

boton3.grid(row= 4, column= 3, padx= 5, pady= 5)
boton2.grid(row= 4, column= 2, padx= 5, pady= 5)
boton1.grid(row= 4, column= 1, padx= 5 , pady= 5)
boton_res.grid(row= 4, column= 4, padx= 5, pady=5)

boton0.grid(row= 5, column= 1, columnspan=2,padx= 5, pady=5)
boton_punto.grid(row= 5, column= 3, padx= 5, pady=5)
boton_igual.grid(row= 5, column= 5, padx= 5, pady=5)

boton_pot.grid(row= 1, column= 3, padx= 5, pady=5)
boton_raiz.grid(row= 2, column= 5, padx= 5, pady=5)
boton_log.grid(row= 3, column= 5, padx= 5, pady=5)
boton_ln.grid(row= 4, column= 5, padx= 5, pady=5)
boton_pi.grid(row= 5, column= 4, padx= 5, pady=5)

boton_Borrar.grid(row= 1, column= 5, padx= 5, pady=5)
boton_sen.grid(row= 2, column= 0, padx= 5, pady=5)
boton_cos.grid(row= 3, column= 0, padx= 5, pady=5)
boton_tan.grid(row= 4, column= 0, padx= 5, pady=5)
boton_euler.grid(row= 5, column= 0, padx= 5, pady=5)


ventana.mainloop()