from tkinter import *
import math

#===================================================
#
#                     bibliotecas
#
#===================================================

def getinputx(): #fazer funcionar inicio
    MX=inputx.get("1.0","end")
    print("Valor de x = ",MX)

def getinputy(): #fazer funcionar inicio
    MY=inputy.get("1.0","end")
    print("Valor de y = ",MY)

#===================================================
#
#                      backend
#
#====================================================

inicio = Tk()
inicio.title("Calculadora Matrizes")
inicio.geometry("610x500+400+100")
inicio['bg'] = '#C58282'

widget1_1 = Frame(inicio)
widget1_1.grid(ipadx=185)
widget1_1['bg'] = '#C58282'

widget2_1 = Frame(inicio)
widget2_1.grid()
widget2_1['bg'] = '#C58282'

widget3_1 = Frame(inicio)
widget3_1.grid(ipadx=110, ipady=20)
widget3_1['bg'] = '#C58282'

widget4_1 = Frame(inicio)
widget4_1.grid(ipadx=225)
widget4_1['bg'] = '#C58282'

widget5_1 = Frame(inicio)
widget5_1.grid(ipadx=205,ipady=10)
widget5_1['bg'] = '#C58282'

widget6_1 = Frame(inicio)
widget6_1.grid(ipadx=255,ipady=10)
widget6_1['bg'] = '#C58282'

widget7_1 = Frame(inicio)
widget7_1.grid()
widget7_1['bg'] = '#C58282'

h1 = Label(widget1_1, text = "Escolha Calculo", foreground='white')
h1['bg'] = '#C58282'
h1["font"] = ("Inter", "25")

bmult = Button(widget2_1, text="Multiplicar", width=10)
bmult.config(font = ("Inter", "20"))

h2 = Label(widget3_1, text = "Tipo Matriz X", foreground='white')
h2['bg'] = '#C58282'
h2["font"] = ("Inter", "25")

h3 = Label(widget3_1, text = "Tipo Matriz Y", foreground='white')
h3['bg'] = '#C58282'
h3["font"] = ("Inter", "25")

inputx = Text(widget4_1, height=2, width=10)
inputy = Text(widget4_1, height=2, width=10)

h4 = Label(widget5_1, text = "Ex: 2:2", foreground='white')
h4['bg'] = '#C58282'
h4["font"] = ("Inter", "25")

h5 = Label(widget5_1, text = "Ex: 2:2", foreground='white')
h5['bg'] = '#C58282'
h5["font"] = ("Inter", "25")

bx = Button(widget6_1, text="Ok", width=6, command=getinputx)
bx.config(font = ("Inter", "10"))

by = Button(widget6_1, text="Ok", width=6, command=getinputy)
by.config(font = ("Inter", "10"))

#tela 2 matrizes

def mudartelaEM(): #ponto de parada dia 04/04 seguir !!!!!!!

    #===================================================
    #
    #                      backend2
    #
    #====================================================

    inicio.destroy()
    global matriz
    matriz = Tk()
    matriz.title("Definir Matrizes")
    matriz.geometry("610x500+400+100")
    matriz['bg'] = '#C58282'

    widget1_2 = Frame(matriz)
    widget1_2.grid(ipadx=192)
    widget1_2['bg'] = '#C58282'

    widget2_2 = Frame(matriz)
    widget2_2.grid(ipadx=140, ipady=30)
    widget2_2['bg'] = '#C58282'
    
    widget3_2 = Frame(matriz)
    widget3_2.grid(ipadx=180, ipady=30)
    widget3_2['bg'] = '#C58282'

    widget4_2 = Frame(matriz)
    widget4_2.grid(ipadx=185)
    widget4_2['bg'] = '#C58282'

    h6 = Label(widget1_2, text = "Insira os valores", foreground='white')
    h6['bg'] = '#C58282'
    h6["font"] = ("Inter", "25")

    h7 = Label(widget2_2, text = "Tabela 1", foreground='white')
    h7['bg'] = '#C58282'
    h7["font"] = ("Inter", "25")
    
    h8 = Label(widget2_2, text = "Tabela 2", foreground='white')
    h8['bg'] = '#C58282'
    h8["font"] = ("Inter", "25")

    h9 = Label(widget3_2, text = "Valor X", foreground='white')
    h9['bg'] = '#C58282'
    h9["font"] = ("Inter", "20")

    h10 = Label(widget3_2, text = "Valor Y", foreground='white')
    h10['bg'] = '#C58282'
    h10["font"] = ("Inter", "20")

    inputmx = Text(widget4_2, height=2, width=10)
    inputmy = Text(widget4_2, height=2, width=10)




    #===================================================
    #
    #                     interface2
    #
    #====================================================

    h6.pack()
    h7.pack(side=LEFT, expand=YES)
    h8.pack(side=LEFT, expand=YES)
    h9.pack(side=LEFT, expand=YES)
    h10.pack(side=LEFT, expand=YES)
    inputmx.pack(side=LEFT, expand=YES)
    inputmy.pack(side=LEFT, expand=YES)

    #===================================================
    #
    #                      Console
    #
    #====================================================



avi = Button(widget7_1, text="Avançar", width=10, command=mudartelaEM)
avi.config(font = ("Inter", "15")) #Verifcador Tela 1

#===================================================
#
#                     interface
#
#====================================================

MX=inputx.get("1.0", "end")
MY=inputy.get("1.0","end")

h1.pack()
bmult.pack()
h2.pack(side=LEFT, expand=YES)
h3.pack(side=LEFT, expand=YES)
inputx.pack(side=LEFT, expand=YES)
inputy.pack(side=LEFT, expand=YES)
h4.pack(side=LEFT, expand=YES)
h5.pack(side=LEFT, expand=YES)
bx.pack(side=LEFT, expand=YES)
by.pack(side=LEFT, expand=YES)
avi.pack()
#pagina inicial

mainloop()

#===================================================
#
#                      Console
#
#====================================================