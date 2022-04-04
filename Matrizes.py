from tkinter import *
import math
from turtle import *

#===================================================
#
#                     bibliotecas
#
#===================================================



#===================================================
#
#                      backend
#
#====================================================

inicio = Tk()
inicio.title("Calculadora Matrizes")
inicio.geometry("600x500+400+100")
inicio['bg'] = '#C58282'

widget1 = Frame(inicio)
widget1.grid(ipadx=140)
widget1['bg'] = '#C58282'
widget2 = Frame(inicio)
widget2.grid()
widget2['bg'] = '#C58282'

h1 = Label(widget1, text = "Escolha Calculo", foreground='white')
h1['bg'] = '#C58282'
h1["font"] = ("Inter", "32")

bmult = Button(widget2, text="Multiplicar")

#===================================================
#
#                     interface
#
#====================================================

h1.pack()
bmult.pack()
mainloop()
#===================================================
#
#                      Console
#
#====================================================