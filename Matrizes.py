from tkinter import *
import math

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
widget1.grid(ipadx=185)
widget1['bg'] = '#C58282'

widget2 = Frame(inicio)
widget2.grid()
widget2['bg'] = '#C58282'

widget3 = Frame(inicio)
widget3.grid(ipadx=110)
widget3['bg'] = '#C58282'

h1 = Label(widget1, text = "Escolha Calculo", foreground='white')
h1['bg'] = '#C58282'
h1["font"] = ("Inter", "25")

bmult = Button(widget2, text="Multiplicar", width=10)
bmult.config(font = ("Inter", "20"))

h2 = Label(widget3, text = "Tipo Matriz X", foreground='white')
h2['bg'] = '#C58282'
h2["font"] = ("Inter", "25")

h3 = Label(widget3, text = "Tipo Matriz Y", foreground='white')
h3['bg'] = '#C58282'
h3["font"] = ("Inter", "25")

#===================================================
#
#                     interface
#
#====================================================

h1.pack()
bmult.pack()
h2.pack(side=LEFT, expand=YES)
h3.pack(side=LEFT, expand=YES)
mainloop()

#===================================================
#
#                      Console
#
#====================================================