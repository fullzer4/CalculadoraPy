from re import A
import numpy as np

AX= int(input("AX: "))
BX= int(input("BX: "))
CX= int(input("CX: "))
DX= int(input("DX: "))

AY= int(input("AY: "))
BY= int(input("BY: "))
CY= int(input("CY: "))
DY= int(input("DY: "))

Mxa = np.array([[AX, BX],
       [CX, DX]])
Mya = np.array([[AY, BY],
       [CY, DY]])

print(Mxa @ Mya)
#funciona