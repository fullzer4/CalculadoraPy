from ast import Mult
from tkinter import *
import math

Mult = 0
Somar = 0

def ClickMult():
    print("ClickMult")
    Mult == 1
    Somar == 0

def ClickSomar():
    print("ClickSomar")
    Somar == 0
    Mult == 1

def VerificarClcik():
    print("Verificado")
    

inicio = Tk()
inicio.title("Calculadora Matrizes")
inicio.geometry("610x500+400+100")
inicio['bg'] = '#C58282'

widget1_1 = Frame(inicio)
widget1_1.grid(ipadx=85)
widget1_1['bg'] = '#C58282'

bmult = Button(widget1_1, text="Multiplicar", width=10, command=ClickMult)
bmult.config(font = ("Inter", "20"))

bsomar = Button(widget1_1, text="Somar", width=10, command=ClickSomar)
bsomar.config(font = ("Inter", "20"))

bmult.pack(side=LEFT, expand=YES)
bsomar.pack(side=LEFT, expand=YES)
mainloop()